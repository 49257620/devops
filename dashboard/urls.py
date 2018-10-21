# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.conf.urls import url, include
from .views import index, loginView,userList

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', loginView, name='login'),
    url(r'userList/$', userList, name='userList')
]
