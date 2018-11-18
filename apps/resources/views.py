from django.http import HttpResponse, JsonResponse, QueryDict
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
import logging
from resources.aliyun import ecs
from rest_framework.viewsets import ReadOnlyModelViewSet
from resources.models import Server,Ip,Cloud
from resources.serializer import ServerSerializer
from rest_framework.pagination import PageNumberPagination


class TestView(View):
    def get(self, request, *args, **kwargs):
        ecs.getEcsList()
        return HttpResponse('test view!')


class ServerViewSet(ReadOnlyModelViewSet):
    queryset = Server.objects.all().order_by('id')
    serializer_class = ServerSerializer





