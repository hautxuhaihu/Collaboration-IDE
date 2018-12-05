"""Collaboration_IDE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from accounts.views import formhandleview
from dashboard.views import home, joinproject, createproject
from ide.views import ide, Messages, Overview, CreateFile, CreateFolder


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$' , formhandleview, name="form"),
    url(r'^home$', home, name='home'),
    url(r'^logout$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^ide/(?P<pk>[0-9]+)/$', ide, name='ide'),
    url(r'^joinproject/$', joinproject, name='joinproject'),
    url(r'^createproject/$', createproject, name='createproject'),
    url(r'^messages/(?P<pk>[0-9]+)/$', Messages, name='messages'),
    url(r'^overview/(?P<pk>[0-9]+)/$', Overview, name='overview'),
    url(r'^createFile/(?P<pk>[0-9]+)/$', CreateFile, name='createFile'),
    url(r'^createFolder/(?P<pk>[0-9]+)/$', CreateFolder, name='createFolder'),

]