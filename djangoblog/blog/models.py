# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
from tagging.fields import TagField
# Create your models here.



@python_2_unicode_compatible
class Blog(models.Model): # 유저 당 하나
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='blog/profile')
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,allow_unicode=True)
    # 블로그 생성한 시각
    # 저장 경로: MEDIA_ROOT/blog/projile/xxx.jpg 파일 저장
    # DB 필드 'MEDIA_URL/blog/profile/xxx.jpg' 문자열 저장
    user = models.OneToOneField(User)
    class Meta:
        ordering = ['-create_date']
        # 생성된 날짜의 내림차순으로 정렬
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=10)
    Blog = models.SlugField(default='slug')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    slug = models.SlugField(allow_unicode=True,default='slug')
    category = models.ForeignKey(Category,null=True,blank=True)
    tag = TagField() # blank= True

    class Meta :
        ordering = ['-create_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=(self.id,))
    # post.get_absolute_url args
    # 객체가 지칭하는 url 반환
    def get_previous_post(self):
        return self.get_previous_by_create_date()
    #create_date 기준으로 이전 포스트 반환
    # get_previous_by_column 내장객체 호출
    def get_next_post(self):
        return self.get_next_by_create_date()

@python_2_unicode_compatible
class Reple(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User)
    Post = models.IntegerField() # post_id
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']
    def __str__(self):
        return self.content










