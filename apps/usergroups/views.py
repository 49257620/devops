from django.http import HttpResponse, JsonResponse, QueryDict
from rest_framework.decorators import action

from idc.models import Idc
from idc.serializer import IdcSerializer, UserSerializer, GroupSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth.models import User, Group, Permission
from .serializer import UserSerializer, UserSerializerV2, GroupSerializer, GroupUsersSerializer, PermissionSerializer, \
    UserGroupsSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from usergroups.filters import UserFilter


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerV2
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserFilter
    filter_fields = ('username',)


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(methods=['get', 'post'], detail=True, serializer_class=GroupUsersSerializer, url_path='user_set')
    def user_set(self, request, *args, **kwargs):
        # self.serializer_class = UserGroupsSerializer
        if self.request.method == 'GET':
            grp = Group.objects.get(**kwargs)
            queryset = grp.user_set.all()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        elif self.request.method == 'POST':
            grp = Group.objects.get(pk=kwargs['pk'])
            uid = request.POST.get('id')
            user = User.objects.get(pk=uid)
            grp.user_set.add(user)
            return Response(status=status.HTTP_201_CREATED)


class UserGroupsViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def get_group_objects(self):
        grp = Group.objects.get(**self.kwargs)
        # print(grp)
        return grp

    def get_queryset(self):
        return self.get_group_objects().user_set.all()

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # uid = JSONParser().parse(request).get('uid')
        # gid = JSONParser().parse(request).get('gid')
        param = JSONParser().parse(request)
        uid = param.get('uid')
        gid = param.get('gid')
        grp = Group.objects.get(pk=gid)
        user = User.objects.get(pk=uid)
        grp.user_set.add(user)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        param = JSONParser().parse(request)
        uid = param.get('uid')
        gid = param.get('gid')
        grp = Group.objects.get(pk=gid)
        user = User.objects.get(pk=uid)
        grp.user_set.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
