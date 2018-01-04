# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

@python_2_unicode_compatible
class Blog(models.Model): # 유저 당 하나
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='blog/profile')
    create_date = models.DateTimeField(auto_now_add=True)
    # 블로그 생성한 시각
    # 저장 경로: MEDIA_ROOT/blog/projile/xxx.jpg 파일 저장
    # DB 필드 'MEDIA_URL/blog/profile/xxx.jpg' 문자열 저장
    user = models.OneToOneField(User,null=True)
    class Meta:
        ordering = ['-create_date']
        # 생성된 날짜의 내림차순으로 정렬
    def __str__(self):
        return self.name
