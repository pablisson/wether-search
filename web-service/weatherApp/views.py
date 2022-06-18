from rest_framework import viewsets
from weatherApp.models import ClimaTempo
from weatherApp.serializer import ClimaTempoSerializer

class ClimaTempoViewSet(viewsets.ModelViewSet):
  queryset = ClimaTempo.objects.all()
  serializer_class = ClimaTempoSerializer