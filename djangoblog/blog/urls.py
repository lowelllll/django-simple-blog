from django.conf.urls import url
from .views import *

app_name = 'blog'
urlpatterns = [
    url(r'^$',BlogLV.as_view(),name="index"),
    url(r'^create/$',BlogCV.as_view(),name='blog_create'),
    url(r'^(?P<slug>[-\w]+)/$',BlogDV.as_view(),name='blog_detail'),
    url(r'^(?P<slug>[-\w]+)/post/create/$',PostCreateView.as_view(),name='post_create'),
    url(r'^(?P<slug>[-\w]+)/post/$',PostLV.as_view(),name='post_list'),
    url(r'^(?P<slug>[-\w]+)/post/(?P<pk>[0-9]+)/$', PostDV.as_view(), name='post_detail'),
    url(r'^(?P<slug>[-\w]+)/update/(?P<pk>[0-9]+)/$', PostUV.as_view(), name='post_update'),
    url(r'^(?P<slug>[-\w]+)/delete/(?P<pk>[0-9]+)/$', PostDeleteView.as_view(), name='post_delete'),
]