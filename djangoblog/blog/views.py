# -*- coding:UTF-8 -*-
from django.shortcuts import render
from .models import Blog
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from djangoblog.views import LoginRequiredMixin
from django.views.generic.detail import DetailView
# Create your views here.


class BlogLV(LoginRequiredMixin,ListView):
    model = Blog
class BlogCV(LoginRequiredMixin,CreateView): # blog_form.html
    model = Blog
    fields = ['name','description','image']
    success_url = reverse_lazy('blog:index')
    def form_valid(self, form): #오류
        form.instance.user = self.request.user #user 설정
        return super(BlogCV,self).form_valid(form)


