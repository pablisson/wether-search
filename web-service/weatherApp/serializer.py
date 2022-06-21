from rest_framework import serializers
from weatherApp.models import Weather, Region

class WeatherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Weather  
    fields = '__all__'
    #list_select_related = ('id','description')

class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = ['name']
    #list_select_related = ('id','name')