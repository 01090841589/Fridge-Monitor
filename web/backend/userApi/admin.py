from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# @admin.register(User)
# class userAdmin(admin.ModelAdmin):
#     list_display = ['id','username','email']

@admin.register(ingredients)
class foodAdmin(admin.ModelAdmin):
    list_display = ['user','name','section','floor','created_at', 'expire_date', 'image', 'classification', 'content', ]

