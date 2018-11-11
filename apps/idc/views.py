from django.http import HttpResponse, JsonResponse, QueryDict
from idc.models import Idc
from idc.serializer import IdcSerializer,UserSerializer,GroupSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.


###################################第一版####################################
class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        content = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(content=content, **kwargs)


# /idcs/
def idc_list(request, *args, **kwargs):
    if request.method == 'GET':
        # 列表
        queryset = Idc.objects.all()
        list_ser = IdcSerializer(queryset, many=True)
        return JSONResponse(list_ser.data)

    elif request.method == 'POST':
        content = JSONParser().parse(request)
        ser = IdcSerializer(data=content)

        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data)


# /idcs/pk
def idc_detail(request, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        # 详细
        ser = IdcSerializer(idc)
        return JSONResponse(ser.data)
    elif request.method == 'PUT':
        # 修改
        content = JSONParser().parse(request)
        ser = IdcSerializer(idc, data=content)

        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data)
    elif request.method == 'DELETE':
        # 删除
        idc.delete()
        return HttpResponse(status=204)


###################################第二版####################################
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# /idcs/
@api_view(['GET', 'POST'])
def idc_list_v2(request, *args, **kwargs):
    if request.method == 'GET':
        # 列表
        queryset = Idc.objects.all()
        list_ser = IdcSerializer(queryset, many=True)
        return Response(list_ser.data)

    elif request.method == 'POST':
        content = JSONParser().parse(request)
        ser = IdcSerializer(data=content)

        if ser.is_valid():
            ser.save()
            return Response(ser.data, status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# /idcs/pk
@api_view(['GET', 'PUT', 'DELETE'])
def idc_detail_v2(request, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # 详细
        ser = IdcSerializer(idc)
        return Response(ser.data)
    elif request.method == 'PUT':
        # 修改
        content = JSONParser().parse(request)
        ser = IdcSerializer(idc, data=content)

        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # 删除
        idc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None, *args, **kwargs):
    return Response({
        'idcs': reverse("idc_list", request=request, format=format)
    })


###################################第三版####################################

from rest_framework.views import APIView


class IdcList(APIView):

    def get(self, request, format=None):
        # 列表
        queryset = Idc.objects.all()
        list_ser = IdcSerializer(queryset, many=True)
        return Response(list_ser.data)

    def post(self, request, format=None):
        ser = IdcSerializer(data=request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data, status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


from django.http import Http404


class IdcDetail(APIView):
    def get_object(self, pk):
        try:
            idc = Idc.objects.get(pk=pk)
            return idc
        except Idc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        idc = self.get_object(pk)
        ser = IdcSerializer(idc)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        idc = self.get_object(pk)
        ser = IdcSerializer(idc, data=request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###################################第四版####################################

from rest_framework import generics, mixins


class IdcList_V4(generics.GenericAPIView,
                 mixins.ListModelMixin,  # 列表
                 mixins.CreateModelMixin):  # 创建
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IdcDetail_V4(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,  # 获取单条记录
                   mixins.UpdateModelMixin,  # 更新记录
                   mixins.DestroyModelMixin):  # 删除记录
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


###################################第五版####################################

class IdcList_V5(generics.ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


class IdcDetail_V5(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


###################################第六版####################################

from rest_framework import viewsets


class IdcViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,  # 列表
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,  # 获取单条记录
                 mixins.UpdateModelMixin,  # 更新记录
                 mixins.DestroyModelMixin):
    # viewsets.ModelViewSet
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


###################################弟七版####################################

class IdcViewSet_V7(viewsets.ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


from django.contrib.auth.models import User, Group,Permission
from idc.serializer import IdcSerializer,UserSerializer,GroupSerializer,PermissionSerializer,UserGroupsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionsViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserGroupsList(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except Idc.DoesNotExist:
            raise Http404

    def get(self, pk,request, format=None):
        # 列表
        queryset = self.get_object(pk).groups.all()
        list_ser = UserGroupsSerializer(queryset, many=True)
        return Response(list_ser.data)

    def post(self, request, format=None):
        ser = IdcSerializer(data=request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data, status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserGroupsDetail(APIView):
    pass