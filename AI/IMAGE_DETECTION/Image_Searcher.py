import os
import sys
import csv
import argparse
from keras_yolo3.yolo import YOLO, detect_video
from PIL import Image
from timeit import default_timer as timer
from Utils.utils import load_extractor_model, load_features, parse_input, detect_object
import test
from Utils import utils
import pandas as pd
import numpy as np
from Utils.Get_File_Paths import GetFileList
import random

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

if __name__ == "__main__":
    input_paths = GetFileList(image_test_folder)
    img_endings = (".jpg", ".jpg", ".png")
    vid_endings = (".mp4", ".mpeg", ".mpg", ".avi")

    input_image_paths = []
    input_video_paths = []
    for item in input_paths:
        if item.endswith(img_endings):
            input_image_paths.append(item)
        elif item.endswith(vid_endings):
            input_video_paths.append(item)

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
        for i, img_path in enumerate(input_image_paths):
            print(img_path)
            prediction, image = detect_object(
                yolo,
                img_path,
                save_img=True,
                save_img_path=detection_results_folder,
                postfix='_detect',
            )
            y_size, x_size, _ = np.array(image).shape
            for single_prediction in prediction:
                out_df = out_df.append(
                    pd.DataFrame(
                        [
                            [
                                os.path.basename(img_path.rstrip("\n")),
                                img_path.rstrip("\n"),
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

    yolo.close_session()

    data_folder = os.path.join(src_path, 'Data\\Results\\Detection_Results.csv')
    label_path = os.path.join(src_path, 'Data\\Model_Weights\\data_classes.txt')
    class_file = open(label_path, "r")
    input_labels = [line.rstrip("\n") for line in class_file.readlines()]
    rownum = 0

    for file in os.scandir(src_path+'\\crop_img'):
        os.remove(file.path)

    dec_img = dict()
    with open(data_folder, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
        
            if rownum == 0:
                header = r
                rownum += 1
                continue
            img = Image.open(r[1])

            print(rownum, float(r[7]))

            if not dec_img.get(input_labels[int(r[6])]):
                dec_img[input_labels[int(r[6])]] = [r[7], r[1], int(r[2]), int(r[3]), int(r[4]), int(r[5])]
            else:
                if dec_img[input_labels[int(r[6])]][0] < r[7]:
                    dec_img[input_labels[int(r[6])]] = [r[7], r[1], int(r[2]), int(r[3]), int(r[4]), int(r[5])]
            rownum += 1

        for key, value in dec_img.items():
            print(key, value)
            img = Image.open(value[1])
            area = (value[2], value[3], value[4], value[5])
            cropped_img = img.crop(area)
            cropped_img = cropped_img.convert("RGB")
            cropped_img.save('.\\crop_img\\'+key+'.jpg')
            
