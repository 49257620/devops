# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission, ContentType

User = get_user_model()


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer()

    def to_representation(self, instance):
        ret = {}
        ret['key'] = instance.id
        ret['label'] = instance.content_type.app_label + '.' + instance.codename
        return ret

    class Meta:
        model = Permission
        fields = "__all__"
