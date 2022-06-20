from rest_framework import serializers
from weatherApp.models import ClimaTempo, Cidade

class ClimaTempoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClimaTempo
    fields = ['data', 'temperatura', 'pressao', 'humidade', 'vento', 'umidade', 'descricao', 'icon', 'cidade', 'estado', 'pais', 'latitude', 'longitude']

class CidadeSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Cidade
    fields = ['id','nome']
    list_select_related = ('id','nome')