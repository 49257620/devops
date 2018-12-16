from rest_framework.response import Response

from rest_framework import status

# Create your views here.
from rest_framework import viewsets, mixins

from .serializer import UserGroupsSerializer, GroupSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .filters import GroupFilter

User = get_user_model()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    filter_fields = ("name",)


class UserGroupViewSet(viewsets.GenericViewSet,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserGroupsSerializer

    def update(self, request, *args, **kwargs):
        userObj = self.get_object()
        groupObjs = request.data.get("gids", [])
        userObj.groups = Group.objects.filter(id__in=groupObjs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        userObj = self.get_object()
        queryset = userObj.groups.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

from django.db.models import Q

class GroupMemberList(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Group.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        groupObj = self.get_object()
        userObjs = groupObj.user_set.all()

        page = self.paginate_queryset(userObjs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(userObjs, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        groupObj = self.get_object()
        userObjs = groupObj.user_set.all()

        groupObj.user_set = groupObj.user_set.filter(~Q(id= request.data.get("uid", '')))

        return Response(status=status.HTTP_204_NO_CONTENT)



class GroupMemberNoList(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Group.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        groupObj = self.get_object()
        userObjs = User.objects.filter(~Q(id__in=[ x.id for x in groupObj.user_set.all()]))

        page = self.paginate_queryset(userObjs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(userObjs, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        groupObj = self.get_object()
        userObjs = groupObj.user_set.all()

        groupObj.user_set = groupObj.user_set.filter(~Q(id= request.data.get("uid", '')))

        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        groupObjs = self.get_object()
        userIds = request.data.get("uids", [])
        print(userIds)
        users = User.objects.filter(id__in=userIds)
        print(users)
        print(groupObjs.user_set)
        for x in users:
            groupObjs.user_set.add(x)


        return Response(status=status.HTTP_204_NO_CONTENT)


