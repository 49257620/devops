# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from rest_framework import serializers
from idc.models import Idc
from django.contrib.auth.models import User, Group, Permission


class UserSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},
        }


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, label='用户ID', help_text='用户ID')
    username = serializers.CharField(required=False, label='用户名', help_text='用户名')
    password = serializers.CharField(required=False, label='密码', help_text='密码')
    email = serializers.EmailField(required=False, label='邮件地址', help_text='邮件地址')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class GroupUsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, label='用户ID', help_text='用户ID')
    username = serializers.CharField(read_only=True, label='用户名', help_text='用户名')
    # password = serializers.CharField(required=False,label='密码',help_text='密码')
    email = serializers.EmailField(read_only=True, label='邮件地址', help_text='邮件地址')

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
