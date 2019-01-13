
# Create your views here.
from rest_framework import viewsets,mixins,permissions,response
from .serializer import UserSerializer,UserRegSerializer
from django_filters.rest_framework import DjangoFilterBackend
from usergroups.filters import UserFilter

from django.contrib.auth import get_user_model

User = get_user_model()


class UsersViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    # filter_backends = (DjangoFilterBackend,)
    filter_class = UserFilter
    filter_fields = ('username',)



class UserRegViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer


class UserInfoViewset(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        data = {
            "username": self.request.user.username,
            "name": self.request.user.name,
            "permission": self.request.user.get_all_permissions(),
            "roles": [x.name for x in self.request.user.groups.all()]
        }
        return response.Response(data)