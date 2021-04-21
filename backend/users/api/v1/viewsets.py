from rest_framework import authentication
from users.models import Location
from .serializers import LocationSerializer
from rest_framework import viewsets


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Location.objects.all()
