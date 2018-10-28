# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.conf.urls import url, include
from .views import index, loginView
from . import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', loginView, name='login'),
    url(r'^index/$', views.IndexView.as_view(), name='IndexView'),
    # url(r'^user/(?P<page>[0-9]+)/$', views.UserView.as_view(), name='user'),
    url(r'^user/$', views.UserView.as_view(), name='user'),
    url(r'^group/add/$', views.GroupView.as_view(), name='groupadd'),
    url(r'^group/list/$', views.GroupListView.as_view(), name='grouplist'),
    url(r'^groupuser/$', views.GroupUserView.as_view(), name='groupuser'),
    url(r'^usergroup/$', views.UserGroupView.as_view(), name='usergroup'),
    url(r'^usergroup/add/$', views.UserGroupAddView.as_view(), name='usergroupadd'),
    url(r'^usergroup/del/$', views.UserGroupDelView.as_view(), name='usergroupdel'),

]

"""
url(r'^login/$', loginView, name='login'),
url(r'^userList/$', userList, name='userList'),
# url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.articlesInfoView, name='articlesList'),
# 位置参数url
# url(r'^articles/([0-9]{4})/([0-1][0-9])/([0-3][0-9])/$', views.articlesInfoView, name='articlesList'),
# key value 参数 url
url(r'^articles/(?P<YYYY>[0-9]{4})/(?P<MM>[0-1][0-9])/(?P<DD>[0-3][0-9])/$', views.articlesInfoView, name='articlesList'),
"""
