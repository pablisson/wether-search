from rest_framework import viewsets
from rest_framework.response import Response
from weatherApp.models import Weather, Region
from weatherApp.serializer import WeatherSerializer, RegionSerializer

from django.db.models import Q

#from tekton.router import to_path
import urllib 
import urllib.parse
#import urllib.urlencode
import requests
import jsonpath
import json
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework.generics import GenericAPIView


class UpdateDeletePostViewSet(
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  GenericAPIView):
  queryset = Weather.objects.all()
  serializer_class = WeatherSerializer 

  def delete(self, request, *args, **kwargs):
    print(request)
    return self.destroy(request, *args, **kwargs)

  #@action(detail=False, methods=['DELETE'], url_path='delete')
  def destroy(self, request, *args, **kwargs):
    weather_ = self.get_object()
    print(weather)
    weather_.is_active = False
    weather_.save()
    return Response(data='delete success') 

class WeatherViewSet(viewsets.ModelViewSet):
  queryset = Weather.objects.all()
  serializer_class = WeatherSerializer 
  print(WeatherSerializer.data,"entrou")
  http_method_names = ['get', 'post', 'head', 'delete', 'put']


  def list(self, request):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = WeatherSerializer(queryset, many=True)
    city = request.query_params.get('nome')
    db = request.query_params.get('db')
    print(db)
    print(city)

    if city is not None:    

      if db == 'true':
        item = queryset.filter(city=request.query_params.get('nome') ).values()
        print(item)
        if item.exists():
          return Response(item)
        else: 
          viewer_list = items_for_viewer()
          aux_values = viewer_list.create_jason_list(city)
          return Response(aux_values)
      else:
          viewer_list = items_for_viewer()
          aux_values = viewer_list.create_jason_list(city)
          return Response(aux_values)
    return Response([])

class RegionViewSet(viewsets.ModelViewSet):
  queryset = Region.objects.all()
  serializer_class = RegionSerializer
  
  def create(self, request):
    serializer = RegionSerializer(data=request.data)
    if serializer.is_valid():
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = RegionSerializer(instance=instance)
    #print(serializer.data)
    return Response(serializer.data)

  def list(self, request):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = RegionSerializer(queryset, many=True)
    region = request.query_params.get('nome')
    print(request)
    if region is not None:    
      item = queryset.filter(name=request.query_params.get('nome'))
      if item.exists():
        viewer_list = items_for_viewer()
        aux_values = viewer_list.create_jason_list(region)
        print(aux_values)
        return Response(item)
      else: 
        return Response([])
    return Response(serializer.data)


# classe para buscar dados da web
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
  

# classe para controlar o json
class json_manager:
  def __init__(self):
    self.json_response = None
    self.item_name = 'list'        
  
  def get_weather_by_region(self, region):
    search_data = url_generic_search()
    url = search_data.join_generic_url(region)
    self.json_response = search_data.get_json_from_url(url) 
    return self.json_response

  def get_item_from_json_all(self,name_item):    
    json_items = jsonpath.jsonpath(self.json_response, name_item)
    if json_items is not None:
      return json_items
    return {}

  def get_item_from_json(self, i):
    allItems = self.get_item_from_json_all("list")
    return allItems[0][i]
  
  def size_of_json(self):
    allItems = self.get_item_from_json_all("list")
    if allItems is not None or allItems != {}:
      return len(allItems[0])
    return 0

# classe para organizar os itens e retorná-los
class items_for_viewer:
  def __init__(self):
    self.items = {}
    self.labels = ['dt_txt', 'temp', 'feels_like', 'temp_min','temp_max','pressure','humidity','description','icon','speed','deg','all','dt', 'id', 'name', 'lat','long']
  
  def add_item(self, label, i, item):
    self.items[i][label] = item
  
  def create_jason_list(self, city):
    manager_data = json_manager()
    manager_data.get_weather_by_region(city)  

    allItems = manager_data.get_item_from_json_all("list")
    city = manager_data.get_item_from_json_all("city")
    print(city)

    j = 0
    countItems = manager_data.size_of_json()    
    oldData = ""
    newData = ""
    
    jsonItemFinal = {}
    jsonData = {}
   
    my_list = []
    for i in range(countItems):
      itemAux = manager_data.get_item_from_json(i)
      newData = itemAux['dt_txt'][0:10]
    
      if oldData == "" or oldData != newData:
        self.items[j] = {}
        oldData = itemAux['dt_txt'][0:10]
        
        aux = {}
        aux.update({self.labels[0]: itemAux[self.labels[0]] })        
        aux.update({self.labels[1] : itemAux['main'][self.labels[1]]})
        aux.update({self.labels[2] : itemAux['main'][self.labels[2]]})
        aux.update({self.labels[3] : itemAux['main'][self.labels[3]]})
        aux.update({self.labels[4] : itemAux['main'][self.labels[4]]})
        aux.update({self.labels[5] : itemAux['main'][self.labels[5]]})
        aux.update({self.labels[6] : itemAux['main'][self.labels[6]]})
        aux.update({self.labels[7] : itemAux['weather'][0][self.labels[7]]})
        aux.update({self.labels[8] : itemAux['weather'][0][self.labels[8]]})
        aux.update({self.labels[9] : itemAux['wind'][self.labels[9]]})
        aux.update({self.labels[10] : itemAux['wind'][self.labels[10]]})
        aux.update({self.labels[11] : itemAux['clouds'][self.labels[11]]})
        aux.update({self.labels[12] : itemAux[self.labels[12]]})
                
        aux.update({'city_id' : city[0]['id']})
        aux.update({'city' : city[0]['name']})
  
        aux.update({'lat' : city[0]['coord']['lat']})
        aux.update({'lon' : city[0]['coord']['lon']})

        my_list.append(aux)

        j += 1
        
        auxiliar = jsonpath.jsonpath(self.items, "[0]")
        
    return my_list


