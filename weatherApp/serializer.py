from rest_framework import serializers
from weatherApp.models import ClimaTempo

class ClimaTempoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClimaTempo
    fields = ['data', 'temperatura', 'pressao', 'humidade', 'vento', 'umidade', 'descricao', 'icon', 'cidade', 'estado', 'pais', 'latitude', 'longitude']