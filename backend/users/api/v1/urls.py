from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import LocationViewSet, UserViewSet

router = DefaultRouter()
router.register("location", LocationViewSet)
router.register("user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
