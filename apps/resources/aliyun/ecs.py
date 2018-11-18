# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

REGION = ['cn-qingdao']
from aliyunsdkcore.request import CommonRequest
from . import getAcsClient
import logging
import json
from resources.serializer import ServerSerializer

logger = logging.getLogger(__name__)


def getEcsRagion(region):
    client = getAcsClient()
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('ecs.aliyuncs.com')
    request.set_method('POST')
    request.set_version('2014-05-26')
    request.set_action_name('DescribeInstances')
    request.add_query_param('RegionId', region)
    response = client.do_action_with_exception(request)
    # data = json.loads(str(response, encoding='utf-8'))
    data = json.loads(response)
    # print(data['Instances']['Instance'])

    for instance in data['Instances']['Instance']:
        # print(instance,type(instance))

        saveInstance(instance)


def saveInstance(instance):
    data = {}
    data["cloud"] = "aliyun"
    data["instanceId"] = instance["InstanceId"]
    data["instanceType"] = instance["InstanceType"]
    data["cpu"] = instance["Cpu"]
    data["memory"] = instance["Memory"]
    data["instanceName"] = instance["InstanceName"]
    data["creationTime"] = instance["CreationTime"]
    data["expiredTime"] = instance["ExpiredTime"]
    data["startTime"] = instance["StartTime"]
    data["hostName"] = instance["HostName"]
    data["innerIps"] = instance["VpcAttributes"]['PrivateIpAddress']['IpAddress']
    data["publicIps"] = instance["PublicIpAddress"]['IpAddress']
    # print(data)
    serializer = ServerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        logger.error("serializer.errors: {}", serializer.errors)


def getEcsList():
    for region in REGION:
        try:
            getEcsRagion(region)
        except Exception as e:
            logger.error('ECS实例获取报错：{0}:{1}', region, e.args)
