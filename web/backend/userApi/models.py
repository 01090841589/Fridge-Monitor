from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class inputFile(models.Model):

    image = models.ImageField(blank=False, null=False,)

class refrigeSection(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class ingredients(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True)
    section = models.CharField(blank=True, max_length=20)
    floor = models.IntegerField(default = 0)
    created_at = models.DateField(auto_now_add=True)
    expire_date = models.CharField(max_length=10)
    classification = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
