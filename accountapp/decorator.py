from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):   # 권한이 필요하다 # 권한 부여?
    def decorated(request, *args, **kwargs):    # request <user 확보>
        target_user = User.objects.get(pk=kwargs['pk'])     # get 방식으로 단 한개만 가져온다
        if target_user == request.user:                 # pk 값이 kwargs 에 들어온다 ['pk'] 지정해서 가져온다
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated

    