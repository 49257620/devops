# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.conf.urls import url, include
from .views import TestView


urlpatterns = [
    url(r'^test/$', TestView.as_view(), name='test'),
]
