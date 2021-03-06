# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from rest_framework import serializers
from idc.models import Idc
from django.contrib.auth.models import User, Group,Permission


class IdcSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False,label='IDC名称',help_text='IDC名称')
    address = serializers.CharField(required=False,label='IDC地址',help_text='IDC地址')
    phone = serializers.CharField(required=False,label='IDC电话',help_text='IDC电话')
    email = serializers.EmailField(required=False,label='IDC邮件',help_text='IDC邮件')

    def create(self, validated_data):
        return Idc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('username', instance.name)
        instance.save()
        return instance


class PermissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    content_type_id = serializers.CharField(required=False)
    codename = serializers.CharField(required=False)

    def create(self, validated_data):
        return Permission.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('username', instance.name)
        instance.content_type_id = validated_data.get('content_type_id', instance.content_type_id)
        instance.codename = validated_data.get('codename', instance.codename)
        instance.save()
        return instance


class UserGroupsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.CharField(required=False)
    group_id = serializers.CharField(required=False)

    def create(self, validated_data):
        return Permission.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.group_id = validated_data.get('group_id', instance.group_id)
        instance.save()
        return instance