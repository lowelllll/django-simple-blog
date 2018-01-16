# -*- coding:UTF-8 -*-
from django.shortcuts import render,resolve_url,redirect
from .models import Blog,Post,Category,Buddy
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy,reverse
from django.views.generic.base import TemplateView,View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from djangoblog.views import LoginRequiredMixin
from django.views.generic.detail import DetailView
from blog.forms import PostForm,PostSearchForm
from tagging.models import Tag,TaggedItem
from tagging.views import TaggedObjectList
from django.db.models import Q
# Create your views here.


class BlogLV(LoginRequiredMixin,ListView):
    model = Blog

    # def get_queryset(self):
    #     return Blog.objects.exclude(user=self.request.user)

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

    def get_context_data(self, **kwargs):
        context = super(BlogDV,self).get_context_data(**kwargs)
        context['categorys'] = Category.objects.filter(Blog=self.kwargs['slug'])
        try:
            context['buddy'] = Buddy.objects.get(user=self.request.user,buddy_user=self.kwargs['slug'])
        except:
            pass

        context['follow'] = Buddy.objects.filter(user=self.kwargs['slug']).count()
        context['follower'] = Buddy.objects.filter(buddy_user=self.kwargs['slug']).count()
        return context

# ======== POST ===========

class PostCreateView(LoginRequiredMixin,CreateView):
    template_name = 'blog/post_form.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.id,'slug':self.object.slug })

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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
        context['categorys'] = Category.objects.filter(Blog=self.kwargs['slug'])
        return context

class PostLV(LoginRequiredMixin,ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostLV,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        context['categorys'] = Category.objects.filter(Blog=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs['slug'])


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('blog:post_list', kwargs={'slug':self.object.slug })

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDeleteView,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

class PostUV(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title','content','category','tag']

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.id,'slug':self.object.slug })

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostUV,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context

class PostCLV(LoginRequiredMixin,ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCLV, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        context['categorys'] = Category.objects.filter(Blog=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs['slug'],category=self.kwargs['pk'])

# ======== CATEGORY =========

class CategoryCV(LoginRequiredMixin,CreateView):
    model = Category
    fields = ['title']

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.object.Blog })

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCV,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        context['categorys'] = Category.objects.filter(Blog=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        form.instance.Blog = self.request.user
        return super(CategoryCV,self).form_valid(form)

# ========= TAG =============

class TagTV(TemplateView): # 블로그 전체
    template_name = 'tagging/tagging_cloud.html'

class PostTOL(TaggedObjectList): # 블로그 전체
    model = Post
    template_name = 'tagging/tagging_post_list.html'

# ========= search ===========

class SearchFV(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        word = '%s' %self.request.POST['search_word']

        post_list = Post.objects.filter(
            Q(title__icontains=word)|Q(content__icontains=word),slug=self.kwargs['slug']
        ).distinct()
        # icontains 대소문자를 구분하지 않고 단어가 포함되어있는지 검사

        context = {}
        context['form'] = form
        context['search_term'] = word
        context['object_list'] = post_list
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        context['categorys'] = Category.objects.filter(Blog=self.kwargs['slug'])

        return render(self.request, self.template_name, context)
        #HttpResponse 객체 반환 render()함수는 리다이렉트가 되지 않음

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchFV,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        context['categorys'] = Category.objects.filter(Blog=self.kwargs['slug'])
        return context

# ======== buddy ===========

def Follow(request,slug):

    try:
        buddy = Buddy.objects.get(user=request.user,buddy_user=slug)
    except:
        buddy = Buddy(user=request.user,buddy_user=slug)
        buddy.save()

    return redirect('blog:follow_done',slug)

class FollowDone(TemplateView):
    template_name = 'blog/Follow_done.html'

    def get_context_data(self, **kwargs):
        context = super(FollowDone,self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context