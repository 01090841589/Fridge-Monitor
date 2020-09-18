from rest_framework import serializers
from django.contrib.auth.models import User
from .models import refrigeSection, inputFile, ingredients

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password', 'email']

class UserSerializer(serializers.ModelSerializer):
    # 특정 유저가 가지고 있는 todo 목록들(여러개 -> many=True)
    # todo_set = TodoSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','email','username']
 
class PasswordChangeSerializer(serializers.ModelSerializer):
    # newPassword = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['password',]

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = refrigeSection
        fields = ['name']

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = inputFile
        fields = ['image']

# class ingredientsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ingredients
#         fields = '__all__'