from django.urls import (path, include)
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet


router = DefaultRouter()

router.register('', TaskViewSet, basename='tasks')

tasks_urlpatterns = [
    path('', include(router.urls))
]