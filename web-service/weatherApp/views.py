from rest_framework import viewsets
from rest_framework.response import Response
from weatherApp.models import ClimaTempo, Cidade
from weatherApp.serializer import ClimaTempoSerializer, CidadeSerializer

from django.db.models import Q

#from tekton.router import to_path
import urllib 
import urllib.parse
import requests



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
      #nItem = queryset.filter(Q(nome__icontains=request.query_params.get('nome')))      
      #print(queryset)      
      item = queryset.filter(nome=request.query_params.get('nome'))
      #item = Cidade.objects.filter(nome=request.query_params.get('nome'))
      #item = Cidade.objects.get(nome=request.query_params.get('nome'))
      #item = Cidade.objects.get(nome=request.query_params.get('nome'))
      #serializerItem = CidadeSerializer(item, many=True)
      #print(type(request.query_params.get('nome')))
      #print(type(item))
      #print(serializer.data)
      #return Response(item)
      print(item)
      print(item.values('nome'))

      
      print(region)
      manager_data = url_generic_search()

      url = manager_data.join_generic_url(region)
      print(url)
      #url = join_generic_url()
      #response = requests.get(url)
      #print(response.json())
      
      

      #operUrl = urllib.request.urlopen(url)

      #r = requests.get(url)
      #json_response = r.json()
      #buscaDadosSite(nameRegion)

      return Response(item.values('nome'))
    return Response(serializer.data)





    def buscaDadosSite(region):
      url = "http://api.openweathermap.org/data/2.5/forecast?q="+region+",pt_br&APPID=4b901a81f4942afae9ee8d6657e3e0dd&units=metric"
      operUrl = urllib.request.urlopen(url)
      if(operUrl.getcode()==200):
        data = operUrl.read()
      else:
        print("Error receiving data", operUrl.getcode())
      print(result.content)
      return result.content



class url_generic_search:
  def get_json_from_url(self, url):
    r = requests.get(url)
    json_response = r.json()
    return json_response

  def join_generic_url(self,region):  
    url = 'http://api.openweathermap.org/data/2.5/forecast?'
    params = {'q=' : region,'pt_br&APPID' : '4b901a81f4942afae9ee8d6657e3e0dd', 'units' : 'metric'}   
    return url + urllib.parse.urlencode(params)
  

 

  
  """
  def retrieve(self, request, pk=None):
    queryset = self.get_queryset(self, request)
    serializer = self.get_serializer(queryset, many=True)
    print(dir(serializer.data))
    return Response(serializer.data)
  #name = CidadeSerializer.get_attribute('nome')
"""

  """
  def get_queryset(self, request, *args, **kwargs):
    queryset = super().get_queryset(self, request, *args, **kwargs)
    print(queryset.filter(nome__icontains=self.request.query_params.get('nome', '')))
    
    is_private_query = Q(is_private=True, owner=self.request.user)
    groups_user_is_part_of = self.request.user.groups().values_list('id', flat=True)
    is_not_private_query = Q(is_private=False) & (Q(owner=self.request.user) | Q(groups__id__in=groups_user_is_part_of))

    return queryset.filter(is_private_query | is_not_private_query).order_by('nome')
    """
    #name = self.request.query_params.get('nome', None)
    #print(name)
  #urlBase = ""
  #urlfetch


"""
class CidadeViewSet(
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin, 
  viewsets.GenericViewSet
):
  queryset = Cidade.objects.all()
  serializer_class = CidadeSerializer
  print(CidadeSerializer.data)
  """