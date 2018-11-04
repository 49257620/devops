# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.conf.urls import url, include
import idc.views as idc

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', idc.idc_detail, name='idc_detail'),
    url(r'^$', idc.idc_list, name='idc_list'),
]

############################## 第二版 ##################################
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', idc.api_root),
    url(r'^idcs/(?P<pk>\d+)/$', idc.idc_detail_v2, name='idc_detail'),
    url(r'^idcs/$', idc.idc_list_v2, name='idc_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################## 第三版 ##################################


urlpatterns = [
    url(r'^$', idc.api_root),
    url(r'^idcs/(?P<pk>\d+)/$', idc.IdcDetail.as_view(), name='idc_detail'),
    url(r'^idcs/$', idc.IdcList.as_view(), name='idc_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################## 第四版 ##################################


urlpatterns = [
    url(r'^$', idc.api_root),
    url(r'^idcs/(?P<pk>\d+)/$', idc.IdcDetail_V4.as_view(), name='idc_detail'),
    url(r'^idcs/$', idc.IdcList_V4.as_view(), name='idc_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################## 第五版 ##################################


urlpatterns = [
    url(r'^$', idc.api_root),
    url(r'^idcs/(?P<pk>\d+)/$', idc.IdcDetail_V5.as_view(), name='idc_detail'),
    url(r'^idcs/$', idc.IdcList_V5.as_view(), name='idc_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################## 第六版 ##################################
from .views import IdcViewSet, IdcViewSet_V7

idc_list = IdcViewSet.as_view({
    "get": "list",
    "post": "create"
})

idc_detail = IdcViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "delete": "destroy",
})

urlpatterns = [
    url(r'^$', idc.api_root),
    url(r'^idcs/(?P<pk>\d+)/$', idc_detail, name='idc_detail'),
    url(r'^idcs/$', idc_list, name='idc_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################## 第七版 ##################################

from rest_framework import routers

router = routers.DefaultRouter()
router.register("dics", IdcViewSet_V7)
urlpatterns = [
    url(r'^', include(router.urls)),
]
