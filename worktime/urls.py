from django.urls import path, include
from rest_framework.routers import DefaultRouter
from worktime import views


router = DefaultRouter()
router.register(r'months', views.WorkMonthViewSet)
router.register(r'days', views.WorkDayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
