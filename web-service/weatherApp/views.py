from rest_framework import viewsets
from rest_framework.response import Response
from weatherApp.models import ClimaTempo, Cidade
from weatherApp.serializer import ClimaTempoSerializer, CidadeSerializer

from django.db.models import Q

#from tekton.router import to_path
import urllib 
import urllib.parse
#import urllib.urlencode
import requests
import jsonpath

#import urllib.parse 
#from urllib import urlencode
# try:
#     import urlparse
#     from urllib import urlencode
# except: # For Python 3
#     import urllib.parse as urlparse
#     from urllib.parse import urlencode

#from google.appengine.api import urlfetch
# Usar urlfech.fetch() para obter os dados do climaTempo.json e cidades.json
class ClimaTempoViewSet(viewsets.ModelViewSet):
  queryset = ClimaTempo.objects.all()
  serializer_class = ClimaTempoSerializer 
  #print(dir(ClimaTempoSerializer))
  #print(ClimaTempoSerializer.Meta)
  #print(ClimaTempoSerializer.Meta.fields)
  print(ClimaTempoSerializer.data)
  
class CidadeViewSet(viewsets.ModelViewSet):
  queryset = Cidade.objects.all()
  serializer_class = CidadeSerializer
  #print(dir(CidadeSerializer.data))

  def create(self, request):
    serializer = CidadeSerializer(data=request.data)
    if serializer.is_valid():
      print(request.data['nome'])
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = CidadeSerializer(instance=instance)
    #print(serializer.data)
    return Response(serializer.data)

  def list(self, request):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = CidadeSerializer(queryset, many=True)
    region = request.query_params.get('nome')
    print(region)
    if region is not None:    
      item = queryset.filter(nome=request.query_params.get('nome'))

      print(item)
      print(item.values('nome'))

      print(region)
      manager_data = url_generic_search()

      url = manager_data.join_generic_url(region)
      print(url)

      return Response(item.values('nome'))
    return Response(serializer.data)



class url_generic_search:
  def __init__(self):
    self.base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    self.params = {'pt_br&APPID' : '4b901a81f4942afae9ee8d6657e3e0dd', 'units' : 'metric'} 
    self.json_response = None      

  def get_json_from_url(self, url):
    r = requests.get(url)
    json_response = r.json()
    return json_response

  def join_generic_url(self,region): 
    self.params['q'] = region
    return self.base_url + urllib.parse.urlencode(self.params)
  
  def get_weather_by_region(self, city):
    url = self.join_generic_url(city)
    self.json_response = self.get_json_from_url(url)    
    return self.json_response
  

