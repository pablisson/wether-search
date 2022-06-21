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


class WeatherViewSet(viewsets.ModelViewSet):
  queryset = Weather.objects.all()
  serializer_class = WeatherSerializer 
  print(WeatherSerializer.data)
  
  def create(self, request):
    serializer = RegionSerializer(data=request.data)
    if serializer.is_valid():
      #print(request.data['nome'])
      return Response(serializer.data, status=status.HTTP_201_CREATED)

  def list(self, request):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = WeatherSerializer(queryset, many=True)
    region = request.query_params.get('nome')
    #print(region)
    if region is not None:    
      item = queryset.filter(region=request.query_params.get('region'))

      print(item.exists() )
      if item.exists():
        print(item.values('region'))

        viewer_list = items_for_viewer()
        aux_values = viewer_list.create_jason_list(region)
        print(aux_values)
        return Response(aux_values)
      else: 
        viewer_list = items_for_viewer()
        aux_values = viewer_list.create_jason_list(region)
        Response(aux_values)

    return Response(serializer.data)

class RegionViewSet(viewsets.ModelViewSet):
  queryset = Region.objects.all()
  serializer_class = RegionSerializer
  
  def create(self, request):
    serializer = RegionSerializer(data=request.data)
    if serializer.is_valid():
      #print(request.data['nome'])
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = RegionSerializer(instance=instance)
    #print(serializer.data)
    return Response(serializer.data)

  def list(self, request):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = RegionSerializer(queryset, many=True)
    region = request.query_params.get('nome')
    #print(region)
    if region is not None:    
      item = queryset.filter(name=request.query_params.get('nome'))

      print(item.exists() )
      if item.exists():
        print(item.values('name'))

        viewer_list = items_for_viewer()
        aux_values = viewer_list.create_jason_list(region)
        print(aux_values)
        return Response(aux_values)
      else: 
        return Response([])
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
    if allItems is not None:
      return len(allItems[0])
    return 0


class items_for_viewer:
  def __init__(self):
    self.items = {}
    self.labels = ['dt_txt', 'temp', 'feels_like', 'temp_min','temp_max','pressure','humidity','description','icon','speed','deg','all','dt']
  
  def add_item(self, label, i, item):
    print(item)
    print(label)
    self.items[i][label] = item
  
  def create_jason_list(self, region):
    manager_data = json_manager()
    manager_data.get_weather_by_region(region)  

    allItems = manager_data.get_item_from_json_all("list")
    region = manager_data.get_item_from_json_all("city")
    #print(region)

    #print(itemAux)
    
    j = 0
    countItems = manager_data.size_of_json()    
    oldData = ""
    newData = ""
    for i in range(countItems):
      itemAux = manager_data.get_item_from_json(i)

      newData = itemAux['dt_txt'][0:10]
      #print(newData)
      if oldData == "" or oldData != newData:
        self.items[j] = {}
        oldData = itemAux['dt_txt'][0:10]
        #print(oldData)

        self.items[j][self.labels[0]] = itemAux[self.labels[0]]
        self.items[j][self.labels[1]] = itemAux['main'][self.labels[1]]
        self.items[j][self.labels[2]] = itemAux['main'][self.labels[2]]
        self.items[j][self.labels[3]] = itemAux['main'][self.labels[3]]
        self.items[j][self.labels[4]] = itemAux['main'][self.labels[4]]
        self.items[j][self.labels[5]] = itemAux['main'][self.labels[5]]
        self.items[j][self.labels[6]] = itemAux['main'][self.labels[6]]
        self.items[j][self.labels[7]] = itemAux['weather'][0][self.labels[7]]
        self.items[j][self.labels[8]] = itemAux['weather'][0][self.labels[8]]
        self.items[j][self.labels[9]] = itemAux['wind'][self.labels[9]]
        self.items[j][self.labels[10]] = itemAux['wind'][self.labels[10]]
        self.items[j][self.labels[11]] = itemAux['clouds'][self.labels[11]]
        self.items[j][self.labels[12]] = itemAux[self.labels[12]]
        j += 1

    print(json.dumps(self.items))
    return self.items


