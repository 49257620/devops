# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFilter(django_filters.rest_framework.FilterSet):
    """
    用户过滤类
    """
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username']
