# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from books.models import Publish, Author, Book
from books.serializer import PublishSerializer, AuthorSerializer, BookSerializer


class PublishViewSet(viewsets.ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, permissions.DjangoModelPermissions)
