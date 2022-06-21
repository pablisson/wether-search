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

      #manager_data = url_generic_search()
      #url = manager_data.join_generic_url(region)
      #print(url)
      viewer_list = items_for_viewer()
      viewer_list.create_jason_list(region)

      # manager_data = json_manager()
      # manager_data.get_weather_by_region(region)      #print(manager_data.get_item_from_json_all())
      # print(manager_data.get_item_from_json(0))

      return Response(item.values('nome'))
    return Response(serializer.data)



class url_generic_search:
  def __init__(self):
    self.base_url = 'http://api.openweathermap.org/data/2.5/forecast?pt_br&'
    self.params = {'APPID' : '4b901a81f4942afae9ee8d6657e3e0dd', 'units' : 'metric'} 
    self.json_response = None      

  def get_json_from_url(self, url):
    r = requests.get(url)
    json_response = r.json()
    return json_response

  def join_generic_url(self,region): 
    self.params['q'] = region
    return self.base_url + urllib.parse.urlencode(self.params)
  
  
class json_manager:
  def __init__(self):
    self.json_response = None
    self.item_name = 'list'
  
  def get_weather_by_region(self, region):
    search_data = url_generic_search()
    url = search_data.join_generic_url(region)
    self.json_response = search_data.get_json_from_url(url) 
    return self.json_response

  def get_item_from_json_all(self):    
    return jsonpath.jsonpath(self.json_response, self.item_name)

  def get_item_from_json(self, i):
    main_item = "".join([self.item_name,"[",str(i),"]"])
    return jsonpath.jsonpath(self.json_response, main_item)
  
  def size_of_json(self):
    allItems = self.get_item_from_json_all()
    print(len(allItems[0]))
    if allItems is not None:
      return len(allItems[0])
    return 0


class items_for_viewer:
  def __init__(self):
    self.items = {}
    self.labels = ['dt_txt', 'temp', 'feels_like', 'temp_min','temp_max','pressure','humidity','description','icon','speed','deg','all']
  
  def add_item(self, label, item):
    self.items[label] = item
  
  def create_jason_list(self, region):
    manager_data = json_manager()
    manager_data.get_weather_by_region(region)  
    itemAux = manager_data.get_item_from_json(6)
    allItems = manager_data.get_item_from_json_all()

    j = 0
    dataAux = ""
    countItems = manager_data.size_of_json()
    print(countItems)

    #print(item)
    """
    for i in range(0, 5): 
      itemAux = manager_data.get_item_from_json(i)
      print(itemAux[0][self.labels[0]])
      print(itemAux[0]['main'][self.labels[1]])
      print(itemAux[0]['main'][self.labels[2]])
      print(itemAux[0]['main'][self.labels[3]])
      print(itemAux[0]['main'][self.labels[4]])
      print(itemAux[0]['main'][self.labels[5]])
      print(itemAux[0]['main'][self.labels[6]])

      print(itemAux[0]['weather'][0][self.labels[7]])
      
      print(itemAux[0]['weather'][0][self.labels[8]])
      print(itemAux[0]['wind'][self.labels[9]])
      print(itemAux[0]['wind'][self.labels[10]])
      print(itemAux[0]['clouds'][self.labels[11]])
      #print(itemAux)
"""
    """
    #self.add_item(self.labels[0], itemAux[0][self.labels[0]])
    self.items[self.labels[0]] = itemAux[0][self.labels[0]]
    self.items[self.labels[1]] = itemAux[0]['main'][self.labels[1]]
    self.items[self.labels[2]] = itemAux[0]['main'][self.labels[2]]
    self.items[self.labels[3]] = itemAux[0]['main'][self.labels[3]]
    self.items[self.labels[4]] = itemAux[0]['main'][self.labels[4]]
    self.items[self.labels[5]] = itemAux[0]['main'][self.labels[5]]
    self.items[self.labels[6]] = itemAux[0]['main'][self.labels[6]]

    self.items[self.labels[7]] = itemAux[0]['weather'][0][self.labels[7]]
    
    self.items[self.labels[8]] = itemAux[0]['weather'][0][self.labels[8]]
    self.items[self.labels[9]] = itemAux[0]['wind'][self.labels[9]]
    self.items[self.labels[10]] = itemAux[0]['wind'][self.labels[10]]
    self.items[self.labels[11]] = itemAux[0]['clouds'][self.labels[11]]
"""

    #print(self.items)

      
    """
    for i in range(0, 2): 
      itemAux = manager_data.get_item_from_json(i)
      print(itemAux)
      self.items[self.labels[0]] = itemAux[i][self.labels[0]]
      self.items[self.labels[1]] = itemAux[i]['main'][self.labels[1]]
      self.items[self.labels[2]] = itemAux[i]['main'][self.labels[2]]
      self.items[self.labels[3]] = itemAux[i]['main'][self.labels[3]]
      self.items[self.labels[4]] = itemAux[i]['main'][self.labels[4]]
      self.items[self.labels[5]] = itemAux[i]['main'][self.labels[5]]
      self.items[self.labels[6]] = itemAux[i]['main'][self.labels[6]]
      self.items[self.labels[7]] = itemAux[i]['weather'][0][self.labels[7]]
      self.items[self.labels[8]] = itemAux[i]['weather'][0][self.labels[8]]
      self.items[self.labels[9]] = itemAux[i]['wind'][self.labels[9]]
      self.items[self.labels[10]] = itemAux[i]['wind'][self.labels[10]]
      self.items[self.labels[11]] = itemAux[i]['clouds'][self.labels[11]]
  """  
  
    return self.items
    