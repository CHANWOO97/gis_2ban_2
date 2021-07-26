from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta: # 장고에서 지원되는 문법
        model = Profile            # 사진의 속성 값들을 메타 데이터
        fields = ['image', 'nickname', 'message']