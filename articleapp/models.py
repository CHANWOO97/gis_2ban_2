from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)

    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                               related_name='article', null=True)

    title = models.CharField(max_length=200, null=True) # 문자열 받을 수 있도록 쓰는 함수
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)  # create 일정을 불러온다
    # 값을 따로 설정하지 않아도 DB 자체에서 설정을 한다 "auto_now_add" 인자 사용
