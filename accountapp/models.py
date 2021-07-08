from django.db import models

## 터미널에서 : python manage.py makemigrations

#makemigrations 란 모델의 변경됨을 감지하여 데이터 스키마에 변화를 반영해준 파일 생성
# Create your models here.
class HelloWorld(models.Model): #모델스안에 대문자 모델 상속
    text = models.CharField(max_length=255, null=False) # CharField 문자열(최대길이 255, 공백 조건)

