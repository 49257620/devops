# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from rest_framework.response import Response

from rest_framework import status

# Create your views here.
from rest_framework import viewsets, mixins

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from .serializer import PermissionSerializer

User = get_user_model()


class PermissionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class GroupPermissionViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Group.objects.all()
    serializer_class = PermissionSerializer

    def retrieve(self, request, *args, **kwargs):
        grpObj = self.get_object()
        perObjs = grpObj.permissions.all()

        page = self.paginate_queryset(perObjs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(perObjs, many=True)
        return Response(serializer.data)



    def update(self, request, *args, **kwargs):
        grpObj = self.get_object()
        pids = request.data.get('pids',[])

        grpObj.permissions = Permission.objects.filter(pk__in=pids)

        return Response(status=status.HTTP_200_OK)
