# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class UserGroupsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)

    class Meta:
        model = Group
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    """
    group序列化类
    """
    
    def to_representation(self, instance):
        ret = super(GroupSerializer, self).to_representation(instance)
        ret['userCnt'] = instance.user_set.all().count()
        return ret
    
    class Meta:
        model = Group
        fields = ("id", "name")

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.CharField(required=False)

    class Meta:
        model = Group
        fields = ('id', 'username','email','name')