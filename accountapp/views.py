from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView  ## 중요!

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def hello_world(request):

    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('input')
            new_data = HelloWorld()
            new_data.text = temp
            new_data.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))

        else:
            data_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html',
                          context={'data_list': data_list})

    else:
        return HttpResponseRedirect(reverse('accountapp:login'))  #function에서는 reverse


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 지금 당장이 아니라 나중에 값을 돌려주려고 lazy~
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'



class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        # get 방식 over 라이딩?
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs) # 이거??
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))


    def post(self, request, *args, **kwargs):
        # post 방식 over 라이딩?
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs) # 이거??
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        # get 방식 over 라이딩?
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)  # 이거??
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        # post 방식 over 라이딩?
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)  # 이거??
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))
