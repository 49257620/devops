# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from workorder.models import WorkOrder
from workorder.serializer import WorkOrderSerializer


class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    permission_classes = (IsAuthenticated, permissions.DjangoModelPermissions)

