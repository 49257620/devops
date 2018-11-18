
# Create your views here.
from rest_framework import viewsets
from .serializer import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from usergroups.filters import UserFilter

from django.contrib.auth import get_user_model

User = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = (DjangoFilterBackend,)
    filter_class = UserFilter
    filter_fields = ('username',)


