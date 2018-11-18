# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from . import settings_local


client = AcsClient(settings_local.ALI_ACCESS_KEY_ID, settings_local.ALI_ACCESS_KEY_SECRET, '')
request = CommonRequest()
request.set_accept_format('json')
request.set_domain('ecs.aliyuncs.com')
request.set_method('POST')
request.set_version('2014-05-26')
request.set_action_name('DescribeInstances')
request.add_query_param('RegionId', 'cn-qingdao')
response = client.do_action_with_exception(request)
# python2: print(response)
print(str(response, encoding='utf-8'))
