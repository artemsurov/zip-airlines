from rest_framework.viewsets import ModelViewSet

from .models import AirPlane
from .serializers import AirPlaneSerializer


class AitPlaneViewSet(ModelViewSet):
    queryset = AirPlane.objects.all()
    serializer_class = AirPlaneSerializer
