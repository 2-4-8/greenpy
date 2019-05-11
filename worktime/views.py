from rest_framework import viewsets, permissions, mixins
from worktime.serializers import WorkMonthCreationSerializer, WorkMonthRetrieveSerializer, WorkDaySerializer
from worktime.models import WorkMonth, WorkDay


class WorkMonthViewSet(viewsets.ModelViewSet):
    queryset = WorkMonth.objects.all()
    serializer_class = WorkMonthRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated, )

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
    permission_classes = (permissions.IsAuthenticated, )
