from rest_framework.response import Response
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import UserCreationSerializer,UserSerializer,PasswordChangeSerializer, ImageSerializer, SectionSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from media.AI import Image_Searcher
from .models import ingredients
import os
import datetime, json
from shutil import copyfile

current = datetime.datetime.now()
current = datetime.date(int(str(current)[:4]), int(str(current)[5:7]), int(str(current)[8:10]))

@api_view(['GET'])
@permission_classes((AllowAny,))
def checkOverlap(request):
    username = request.data
    if User.objects.filter(username=username):
        return Response(False)
    else:
        return Response(True)


@api_view(['POST'])
# settings의 isAuthenticated 무시하고 로그인이 되지 않더라도 요청 허용
@permission_classes((AllowAny, ))
def signUp(request):
    serializer = UserCreationSerializer(data=request.data)
    print("username:",serializer.initial_data)
    username = serializer.initial_data.get('username')
    if serializer.is_valid():
        
        # serializer.save()의 return 값은 모델의 인스턴스
        user = serializer.save()
        # User model의 인스턴스가 갖고 있는 set_password -> 인자는 raw password가 들어감
        user.set_password(request.data.get('password'))
        user.save()
        print(serializer.data)
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
    else:
        return Response(serializer.errors, status=400)

user_manage_param = openapi.Parameter('password', openapi.IN_QUERY, type=openapi.TYPE_STRING)
user_response = openapi.Response('response description', UserSerializer)

@swagger_auto_schema(method='put', manual_parameters=[user_manage_param], responses={200: user_response})
@api_view(['GET','PUT','DELETE'])
def user_manage(request, id):
    user = get_object_or_404(User,pk=id)
    # print("user method:",dir(user))
    if request.user != user:
        # Response(status=403) 과 동일
        return HttpResponseForbidden()
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        # 기존 todo에서 request.POST(수정 내용)으로 변경
        serializer = PasswordChangeSerializer(user,request.POST)
        usercheck = serializer
        print(usercheck)
        if serializer.is_valid():
            print('PASSWORD:',request.data.get('password'))
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data)
        # 유효하지 않으면 에러메세지와 함께 400 에러
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        user.delete()
        print("IS_DELETED:",User.objects.filter(pk=id))
        # 204 -> 해당하는 컨텐츠가 없는 경우(todo를 삭제했기 때문에 해당하는 todo가 존재하지 않음을 알려줌)
        return Response(status=204)


@api_view(['POST'])
def get_image(request):
    print(request)
    return Response(status=404)

user_manage_param = openapi.Parameter('image', openapi.IN_QUERY, type=openapi.TYPE_FILE)
user_response = openapi.Response('response description', UserSerializer)

@swagger_auto_schema(method='post', manual_parameters=[user_manage_param], responses={200: user_response})
@api_view(['POST'])
@permission_classes((AllowAny, ))
def test(request):
    # return Response({'message:url&view test success!'})
    # print(dir(request.query_params))
    serializer = ImageSerializer(data=request.data)
    result = Image_Searcher.detector(request.data, request.data.get('username'))
    for file in os.scandir('./media/AI/Data/Test_images/'):
        os.remove(file.path)
    return Response(result)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def addIngredients(request):
    # for req_data in request.data:
    print(request.data)
    if request.method == 'POST':
        # image_file = 

        for req_data in request.data:
            postpone = req_data.get('expirationDate')
            days = current + datetime.timedelta(int(postpone))
            food = ingredients(name=req_data.get('name'),image = req_data.get('iamge'), user_id = req_data.get('user_id'), floor=req_data.get('floor'), expire_date = str(days)[:10], classification = req_data.get('kind'))
            food.save()
        return Response(status=200)
    
@api_view(['GET'])
@permission_classes((AllowAny, ))
def getIngredients(request,id):
    user = User.objects.get(id = id)
    food_lists = ingredients.objects.filter(user_id = id)
    foods = []
    for food_list in food_lists:
        
        if not os.path.exists('./media/AI/crop_img/'+user.username+'/'):
            os.makedirs('./media/AI/crop_img/'+user.username+'/')
        if not os.path.exists('./media/AI/crop_img/'+user.username+'/'+food_list.name[:10]+'.jpg'):
            copyfile('./media/AI/crop_img/no_image.jpg', './media/AI/crop_img/'+user.username+'/'+food_list.name[:10]+'.jpg'    )
            pass  
        food = []
        food.append(food_list.name)
        food.append(food_list.expire_date)
        food.append(food_list.created_at)
        food.append(food_list.classification)
        food.append(food_list.content)
        food.append(food_list.floor)
        postpone = datetime.date(int(food_list.expire_date[:4]), int(food_list.expire_date[5:7]), int(food_list.expire_date[8:]))
        sub_days = postpone - current
        food.append(sub_days.days)
        food.append(food_list.id)
        foods.append(food)
     
    return Response(foods)     

@api_view(['PUT','DELETE'])
@permission_classes((AllowAny, ))
def updateIngredients(request,id):
    data = request.data
    food = ingredients.objects.get(pk=id)
    if request.method =='PUT':
        print(request.data)
        if type(data) == int:
            food.floor = 4-data
            food.save()

        else:

            food.name = data['name']
            food.image = data['img_path']
            food.floor = data['floor']
            date = current + datetime.timedelta(days=int(data['expirationDate']))
            food.expire_date = date
            food.classification = data['category']
            food.content = data['note']
            food.save()
    if request.method =='DELETE':
        food.delete()

        return Response(status=204)
    return Response(data, status=204)