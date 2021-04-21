from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import LocationViewSet

router = DefaultRouter()
router.register("location", LocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
