# -*- coding:UTF-8 -*-
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    template_name = 'index.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDone(TemplateView):
    template_name='registration/register_done.html'

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls,**initkwargs):
        view = super(LoginRequiredMixin,cls).as_view(**initkwargs)
        return login_required(view)

    # LoginRequiredMixin 클래스를 상속받는 클래스의 as_view() 메소드를 호출하면 다중상속 구조의 메소드를 호출하는 순서에 의해
    # view클래스의 as_view() 메소드에  login_required 기능이 적용
