# -*- coding:UTF-8 -*-
from django.shortcuts import render
from .models import Blog,Post,Reple
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from djangoblog.views import LoginRequiredMixin
from django.views.generic.detail import DetailView
# Create your views here.


class BlogLV(LoginRequiredMixin,ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.exclude(user=self.request.user)

class BlogCV(LoginRequiredMixin,CreateView): # blog_form.html
    model = Blog
    fields = ['name','description','image']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form): #오류
        form.instance.user = self.request.user #user 설정
        form.instance.slug = self.request.user
        return super(BlogCV,self).form_valid(form)

class BlogDV(LoginRequiredMixin,DetailView):
    model = Blog

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:index')
    template_name = 'blog/post_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostDV(LoginRequiredMixin,DetailView):
    model = Post
    fields =['title','content']

    def get_context_data(self, **kwargs):
        context = super(PostDV, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

class PostLV(LoginRequiredMixin,ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostLV,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs['slug'])


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDeleteView,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

class PostUV(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title','content']
    success_url = reverse_lazy('blog:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostUV,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

