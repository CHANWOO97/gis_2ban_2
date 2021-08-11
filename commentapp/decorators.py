from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk']) # db 접근할 때 해당클래스
        if target_comment.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated