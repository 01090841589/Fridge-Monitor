import os
import sys
import csv
import argparse
from media.AI.keras_yolo3.yolo import YOLO, detect_video
from PIL import Image
from timeit import default_timer as timer
from media.AI.Utils.utils import load_extractor_model, load_features, parse_input, detect_object
import test
from media.AI.Utils import utils
import pandas as pd
import numpy as np
from media.AI.Utils.Get_File_Paths import GetFileList
from keras import backend
import random
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

infos = {'onion': {'name': '양파',
                    'expirationDate': 7,
                    'kind': '야채',
                    'note': '',},      
        'carrot':{'name': '당근',
                    'expirationDate': 14,
                    'kind': '야채',
                    'note': '',},
        'potato':{'name': '감자',
                    'expirationDate': 5,
                    'kind': '야채',
                    'note': '',},
        'greenOnion':{'name': '대파',
                    'expirationDate': 10,
                    'kind': '야채',
                    'note': '',},
        'garlic':{'name': '마늘',
                    'expirationDate': 14,
                    'kind': '야채',
                    'note': '',},
        'garlicPart':{'name': '마늘',
                    'expirationDate': 14,
                    'kind': '야채',
                    'note': '',}, 
        'tomato_top':{'name': '토마토',
                    'expirationDate': 14,
                    'kind': '야채',
                    'note': '',},
        'tomato_side':{'name': '토마토',
                    'expirationDate': 14,
                    'kind': '야채',
                    'note': '',},
        'green-chili':{'name': '풋고추',
                    'expirationDate': 10,
                    'kind': '야채',
                    'note': '',}, 
        'egg_white':{'name': '계란',
                    'expirationDate': 14,
                    'kind': '야채',
                    'note': '',},
        'egg_brown':{'name': '계란',
                    'expirationDate': 14,
                    'kind': '야채',
                    'note': '',},
        'parprika':{'name': '파프리카',
                    'expirationDate': 21,
                    'kind': '야채',
                    'note': '',},
        'parprika_top':{'name': '파프리카',
                    'expirationDate': 21,
                    'kind': '야채',
                    'note': '',},
        'enoki-mushroom':{'name': '팽이버섯',
                    'expirationDate': 5,
                    'kind': '야채',
                    'note': '',},
        'king_oyster_mushroom':{'name': '느타리버섯',
                    'expirationDate': 5,
                    'kind': '야채',
                    'note': '',},
        'agaricus_bisporus':{'name': '새송이버섯',
                    'expirationDate': 14,
                    'kind': '야채',
                    'note': '',},
        'meat':{'name': '고기',
                    'expirationDate': 3,
                    'kind': '육류',
                    'note': '',},
        'corn':{'name': '옥수수',
                    'expirationDate': 3,
                    'kind': '육류',
                    'note': '',},
        'broccoli':{'name': '브로콜리',
                    'expirationDate': 7,
                    'kind': '육류',
                    'note': '',},
        'raw-chicken':{'name': '닭고기',
                    'expirationDate': 2,
                    'kind': '육류',
                    'note': '',},
        }

src_path = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(src_path, "Utils")
sys.path.append(src_path)
sys.path.append(utils_path)

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3" #Tensorflow 경고 안보이게

data_folder = os.path.join(src_path, "Data")
image_test_folder = os.path.join(data_folder, "Test_Images")
detection_results_folder = os.path.join(data_folder, "Results")
detection_results_file = os.path.join(detection_results_folder, "Detection_Results.csv")
model_folder = os.path.join(data_folder, "Model_Weights")
model_weights = os.path.join(model_folder, "trained_weights_final.h5")
model_classes = os.path.join(model_folder, "data_classes.txt")
anchors_path = os.path.join(src_path, "keras_yolo3", "model_data", "yolo_anchors.txt")

def detector(input_image, username):
    file = input_image["file"]
    if not os.path.exists(image_test_folder):
        os.makedirs(image_test_folder)
    path = default_storage.save(image_test_folder+'\\buf_img.jpg', ContentFile(file.read()))

    
    input_paths = GetFileList(image_test_folder)
    img_endings = (".jpg", ".jpg", ".png")
    vid_endings = (".mp4", ".mpeg", ".mpg", ".avi")
    
    input_img = Image.open(input_paths[0])
    input_image_paths = [input_paths[0]]

    output_path = detection_results_folder
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    yolo = YOLO(
        **{
            "model_path": model_weights,
            "anchors_path": anchors_path,
            "classes_path": model_classes,
            "score": 0.1, #예측의 점수 기준
            "gpu_num": 1,
            "model_image_size": (416, 416),
        }
    )

    out_df = pd.DataFrame(
        columns=[
            "image", "image_path", "xmin", "ymin", "xmax", "ymax", "label", "confidence", "x_size", "y_size",
        ]
    )

    class_file = open(model_classes, "r")
    input_labels = [line.rstrip("\n") for line in class_file.readlines()]
    print("Found {} input labels: {} ...".format(len(input_labels), input_labels))

    if input_image_paths:
        print(
            "Found {} input images: {} ...".format(
                len(input_image_paths),
                [os.path.basename(f) for f in input_image_paths[:5]],
            )
        )

        start = timer()
        text_out = ""

        # This is for images
        prediction, image = detect_object(
            yolo,
            input_paths[0],
            save_img=False,
            save_img_path=detection_results_folder,
            postfix='_detect',
        )
        y_size, x_size, _ = np.array(image).shape
        for single_prediction in prediction:
            out_df = out_df.append(
                pd.DataFrame(
                    [
                        [
                            os.path.basename(input_paths[0].rstrip("\n")),
                            input_paths[0].rstrip("\n"),
                        ]
                        + single_prediction
                        + [x_size, y_size]
                    ],
                    columns=[
                        "image", "image_path", "xmin", "ymin", "xmax", "ymax", "label", "confidence", "x_size", "y_size",
                    ],
                )
            )
        end = timer()
        print(
            "Processed {} images in {:.1f}sec - {:.1f}FPS".format(
                len(input_image_paths),
                end - start,
                len(input_image_paths) / (end - start),
            )
        )
        out_df.to_csv(detection_results_file, index=False)

    # yolo.close_session()
    backend.clear_session()
    data_folder = os.path.join(src_path, 'Data/Results/Detection_Results.csv')
    label_path = os.path.join(src_path, 'Data/Model_Weights/data_classes.txt')
    class_file = open(label_path, "r")
    input_labels = [line.rstrip("\n") for line in class_file.readlines()]
    rownum = 0

    # for file in os.scandir(src_path+'\\crop_img'):
    #     os.remove(file.path)

    dec_img = dict()
    with open(data_folder, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
        
            if rownum == 0:
                header = r
                rownum += 1
                continue
            img = Image.open(r[1])

            if not dec_img.get(input_labels[int(r[6])]):
                dec_img[input_labels[int(r[6])]] = [r[7], r[1], int(r[2]), int(r[3]), int(r[4]), int(r[5])]
            else:
                
                if dec_img[input_labels[int(r[6])]][0] < r[7]:
                    dec_img[input_labels[int(r[6])]] = [r[7], r[1], int(r[2]), int(r[3]), int(r[4]), int(r[5])]
            rownum += 1
        result = []
        for key, value in dec_img.items():
            img = Image.open(value[1])
            area = (value[2], value[3], value[4], value[5])
            cropped_img = img.crop(area)
            cropped_img = cropped_img.convert("RGB")
            if not os.path.exists('./media/AI/crop_img/'+username+'/'):
                os.makedirs('./media/AI/crop_img/'+username+'/')
            nam = infos.get(key).get('name')
            cropped_img.save('./media/AI/crop_img/'+username+'/'+nam+'.jpg')
            result.append(infos[key])


    return result
