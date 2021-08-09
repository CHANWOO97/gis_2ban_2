from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True) # 장고에서 제공해주는 유저 임포트

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True) # db 에 저장되는 순간 타임~
