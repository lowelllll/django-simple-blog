# -*- coding:UTF-8 -*-
"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# ROOT_URLCONF
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(),name="index"),
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'^accounts/',include('django.contrib.auth.urls')), # 장고의 인증기능 URLConf를 가져와서 사용
    url(r'^accounts/register/$',UserCreateView.as_view(),name="register"),
    url(r'^accounts/register/done/$',UserCreateDone.as_view(),name="register_done")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
