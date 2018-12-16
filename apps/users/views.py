
# Create your views here.
from rest_framework import viewsets,mixins
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