from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets, mixins

from .serializer import UserGroupsSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserGroupViewSet(viewsets.GenericViewSet,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserGroupsSerializer

    def update(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        userObj = self.get_object()
        queryset = userObj.groups.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
