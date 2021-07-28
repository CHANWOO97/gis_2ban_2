from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
    # update 문은 pk를 넘겨받아야 무엇을 수정할 지 알 수 있다.

]