# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.conf.urls import url, include
import idc.views as idc


from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register("groups", GroupsViewSet, base_name='groups')
router.register("users", UsersViewSet, base_name='users')
router.register("userGroups", UserGroupsViewSet, base_name='user_group')

urlpatterns = [
    url(r'^', include(router.urls))
]
#urlpatterns = format_suffix_patterns(urlpatterns)