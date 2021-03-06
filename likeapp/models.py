from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like_record', null=False) # 좋아요는 널값이 없어야징

    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='like_record', null=False)

    class Meta:
        unique_together = ['user', 'article']
