# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class UserRegSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, label='密码', write_only=True, help_text='密码')

    def validate(self, attrs):
        attrs['is_active'] = False
        attrs['email'] = "{}{}".format(attrs['username'], settings.DOMAIN)
        return attrs

    def create(self, validated_data):
        instance = super(UserRegSerializer, self).create(validated_data=validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.get("password", None)
        if password:
            instance.set_password(validated_data['password'])
            instance.save()
        return instance

    class Meta:
        model = User
        fields = ("username", 'password', "name", "id", "phone")


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True, label="上次登录时间",
                                           help_text="上次登录时间")
    is_active = serializers.BooleanField(label="是否激活", help_text="是否激活")

    def update(self, instance, validated_data):
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ("id", "username", 'email', "name", "phone", "is_active", "last_login")


class UserSerializer_bak(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},
        }
