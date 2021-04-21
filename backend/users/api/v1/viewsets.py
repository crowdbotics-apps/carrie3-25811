from rest_framework import authentication
from users.models import Location, User
from .serializers import LocationSerializer, UserSerializer
from rest_framework import viewsets


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Location.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = User.objects.all()
