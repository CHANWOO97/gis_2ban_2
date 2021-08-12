from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20, null=False) # 이름을 charfield 를 이용하여 만듬
    description = models.CharField(max_length=200, null=True) # db에 null을 허용하고 안하고를 설정하는 것임
    image = models.ImageField(upload_to='project/', null=False) # media 폴더에 이미지 업로드

    created_at = models.DateTimeField(auto_now_add=True) # 클라이언트에 승인 받지 않아도 자동 생성
