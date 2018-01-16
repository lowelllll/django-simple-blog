from django.conf.urls import url
from .views import *

app_name = 'blog'
urlpatterns = [
    url(r'^$',BlogLV.as_view(),name="index"),
    url(r'^create/$',BlogCV.as_view(),name='blog_create'),
    url(r'^(?P<slug>[-\w]+)/$',BlogDV.as_view(),name='blog_detail'),
    url(r'^(?P<slug>[-\w]+)/post/create/$',PostCreateView.as_view(),name='post_create'),
    url(r'^(?P<slug>[-\w]+)/post$',PostLV.as_view(),name='post_list'),
    url(r'^(?P<slug>[-\w]+)/post/(?P<pk>[0-9]+)/$', PostDV.as_view(), name='post_detail'),
    url(r'^(?P<slug>[-\w]+)/update/(?P<pk>[0-9]+)/$', PostUV.as_view(), name='post_update'),
    url(r'^(?P<slug>[-\w]+)/delete/(?P<pk>[0-9]+)/$', PostDeleteView.as_view(), name='post_delete'),
    url(r'^(?P<slug>[-\w]+)/category/create/$', CategoryCV.as_view(), name='category_create'),
    url(r'^(?P<slug>[-\w]+)/post/category/(?P<pk>[0-9]+)/$', PostCLV.as_view(), name='post_list_category'),
    url(r'^tag/&',TagTV.as_view(),name='tag_cloud'),
    url(r'^(?P<slug>[-\w]+)/tag/(?P<tag>[^/]+(?u))/$',PostTOL.as_view(),name='tagged_object_list'),
    url(r'^(?P<slug>[-\w]+)/search/$',SearchFV.as_view(),name='search'),
    url(r'^(?P<slug>[-\w]+)/buddy/$',Follow,name="follow"),
    url(r'^(?P<slug>[-\w]+)/follow/done/$',FollowDone.as_view(),name="follow_done")
]