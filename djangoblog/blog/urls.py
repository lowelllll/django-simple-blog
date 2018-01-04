from django.conf.urls import url
from .views import *
app_name = 'blog'
urlpatterns = [
    url(r'^$',BlogLV.as_view(),name="index"),
    url(r'^create/',BlogCV.as_view(),name='blog_create'),
]