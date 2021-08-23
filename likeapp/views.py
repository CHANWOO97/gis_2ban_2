from django.shortcuts import render

# Create your views here.
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


class LikeArticleView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        likeRecord = LikeRecord.objects.filter(user=user,
                                               article=article)
        if likeRecord.exists():
           pass
        else:
            pass

        return super().get(request, *args, **kwargs)