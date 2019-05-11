from rest_framework import viewsets, permissions, mixins
from worktime.serializers import (
    WorkMonthCreationSerializer, WorkMonthRetrieveSerializer, WorkDaySerializer, UserSerializer)
from worktime.models import WorkMonth, WorkDay
from worktime.permissions import IsOwnerOrReject
from django.contrib.auth.models import User


class WorkMonthViewSet(viewsets.ModelViewSet):
    queryset = WorkMonth.objects.all()
    serializer_class = WorkMonthRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReject)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            serializer_class = WorkMonthCreationSerializer
        return serializer_class


class WorkDayViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = WorkDay.objects.all()
    serializer_class = WorkDaySerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReject)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
