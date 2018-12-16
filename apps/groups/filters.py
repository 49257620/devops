import django_filters
from django.contrib.auth.models import Group

class GroupFilter(django_filters.rest_framework.FilterSet):
    """
    group过滤类
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Group
        fields = ('name',)