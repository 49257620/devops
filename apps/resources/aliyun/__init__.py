# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
from django.conf import settings
from aliyunsdkcore.client import AcsClient


def getAcsClient():
    return AcsClient(settings.ALI_ACCESS_KEY_ID, settings.ALI_ACCESS_KEY_SECRET, '')
