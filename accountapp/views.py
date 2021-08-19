from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView  ## 중요!
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld
from articleapp.models import Article


@login_required # 장고에서 지원
def hello_world(request):

    if request.user.is_authenticated: # 유저가 로그인 되있을 경우
        if request.method == "POST":

            temp = request.POST.get('input')
            new_data = HelloWorld()
            new_data.text = temp
            new_data.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))

        else:
            data_list = HelloWorld.objects.all() # DB에서 object 객체를 all 모두 긁어온다 이런식으로 데이터베이스 긁어온다
            return render(request, 'accountapp/hello_world.html',
                          context={'data_list': data_list})

    else:
        # 로그인 되지 않은 경우
        return HttpResponseRedirect(reverse('accountapp:login'))  #function에서는 reverse


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    # 지금 당장이 아니라 나중에 값을 돌려주려고 lazy~
    template_name = 'accountapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})




class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,
                                        **kwargs)

# @method_decorator 리스트 기능 가지고 있당
has_ownership = [login_required, account_ownership_required]


@method_decorator(has_ownership, 'get')  #
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})



@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'