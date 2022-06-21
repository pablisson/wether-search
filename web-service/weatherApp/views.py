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
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  

  def list(self, request):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = WeatherSerializer(queryset, many=True)
    city = request.query_params.get('nome')
    db = request.query_params.get('db')
    print(db)
    print(city)

    # requestAux = HttpRequest()
    # requestAux.method = 'POST'
    # finalRequest = Request(requestAux)
    # create()

    if city is not None:    

      if db == True:
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
    print(request)
    if region is not None:    
      item = queryset.filter(name=request.query_params.get('nome'))

      #print(item.exists() )
      if item.exists():
        #print(item.values('name'))

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
    if allItems is not None:
      return len(allItems[0])
    return 0

# classe para organizar os itens e retorná-los
class items_for_viewer:
  def __init__(self):
    self.items = {}
    self.labels = ['dt_txt', 'temp', 'feels_like', 'temp_min','temp_max','pressure','humidity','description','icon','speed','deg','all','dt', 'city']
  
  def add_item(self, label, i, item):
    #print(item)
    #print(label)
    self.items[i][label] = item
  
  def create_jason_list(self, city):
    manager_data = json_manager()
    manager_data.get_weather_by_region(city)  

    allItems = manager_data.get_item_from_json_all("list")
    city = manager_data.get_item_from_json_all("city")
    #print(region)

    #print(itemAux)
    
    j = 0
    countItems = manager_data.size_of_json()    
    oldData = ""
    newData = ""
    
    jsonItemFinal = {}
    jsonData = {}
   
    my_list = []
    for i in range(countItems):
      itemAux = manager_data.get_item_from_json(i)
      #print(itemAux)
      newData = itemAux['dt_txt'][0:10]
      #print(newData)
    
      if oldData == "" or oldData != newData:
        #print(itemAux)
        #print("----------------------------------------")
        #my_list.append(itemAux[self.labels[0]])


        self.items[j] = {}
        oldData = itemAux['dt_txt'][0:10]
        #print(oldData)
        """
        newItem =  '['+self.labels[0] +':'+ itemAux[self.labels[0]] + ','
        self.labels[1] + ':' + itemAux['main'][self.labels[1]] + ','
        self.labels[2] + ':' + itemAux['main'][self.labels[2]] + ','
        self.labels[3] + ':' + itemAux['main'][self.labels[3]] + ','
        self.labels[4] + ':' + itemAux['main'][self.labels[4]] + ','
        self.labels[5] + ':' + itemAux['main'][self.labels[5]] + ','
        self.labels[6] + ':' + itemAux['main'][self.labels[6]] + ','
        self.labels[7] + ':' + itemAux['weather'][0][self.labels[7]] + ','
        self.labels[8] + ':' + itemAux['weather'][0][self.labels[8]] + ','
        self.labels[9] + ':' + itemAux['wind'][self.labels[9]] + ','
        self.labels[10] + ':' + itemAux['wind'][self.labels[10]] + ','
        self.labels[11] + ':' + itemAux['clouds'][self.labels[11]] + ','
        self.labels[12] + ':' + itemAux[self.labels[12]] + ','
        ']'
        """
        """
        #print(newItem)
        #jsonItemFinal = json.loads(newItem)
        self.items[self.labels[0]] = itemAux[self.labels[0]]
        self.items[self.labels[1]] = itemAux['main'][self.labels[1]]
        self.items[self.labels[2]] = itemAux['main'][self.labels[2]]
        self.items[self.labels[3]] = itemAux['main'][self.labels[3]]
        self.items[self.labels[4]] = itemAux['main'][self.labels[4]]
        self.items[self.labels[5]] = itemAux['main'][self.labels[5]]
        self.items[self.labels[6]] = itemAux['main'][self.labels[6]]
        self.items[self.labels[7]] = itemAux['weather'][0][self.labels[7]]
        self.items[self.labels[8]] = itemAux['weather'][0][self.labels[8]]
        self.items[self.labels[9]] = itemAux['wind'][self.labels[9]]
        self.items[self.labels[10]] = itemAux['wind'][self.labels[10]]
        self.items[self.labels[11]] = itemAux['clouds'][self.labels[11]]
        self.items[self.labels[12]] = itemAux[self.labels[12]]
        itemAuxiliar = json.loads(json.dumps(self.items))
        print(itemAuxiliar)

        
        jsonItemFinal.update(itemAuxiliar)

        print(jsonItemFinal)
        """
        
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
        #print(aux)
        
        my_list.append(aux)
        #jsonItemFinal.update([jsonData])
        """
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
        """
        j += 1
        #print(json.dumps(self.items[j]))
        auxiliar = jsonpath.jsonpath(self.items, "[0]")
        
        #jsonItemFinal = auxiliar.update(jsonItemFinal) 

    #print(jsonItemFinal)
    #print(my_list)
    #print(my_list)
    return my_list


