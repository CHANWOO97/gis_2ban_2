from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    # 장고 공식문서에서 사용하는 문장
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style':'min-height : 10rem;'
                                                                    'text-align: left;'}))

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']

