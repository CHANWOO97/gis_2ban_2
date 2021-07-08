from django.db import models

## 터미널에서 : python manage.py makemigrations
# Create your models here.
class HelloWorld(models.Model): #모델스안에 대문자 모델 상속
    text = models.CharField(max_length=255, null=False) # CharField 문자열(최대길이 255, 공백 조건)