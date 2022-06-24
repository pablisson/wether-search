from django.db.models import Q

#from tekton.router import to_path
import urllib 
import urllib.parse
#import urllib.urlencode
import requests
import jsonpath
import json


# classe para buscar dados da web
class UrlGenericSearch:
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
class JsonManager:
  def __init__(self):
    self.json_response = None
    self.item_name = 'list'        
  
  def get_weather_by_region(self, region):
    search_data = UrlGenericSearch()
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



class ItemsForViewer:
  def __init__(self):
    self.items = {}
    self.labels = ['dt_txt', 'temp', 'feels_like', 'temp_min','temp_max','pressure','humidity','description','icon','speed','deg','all','dt', 'id', 'name', 'lat','long','country']
  
  def add_item(self, label, i, item):
    self.items[i][label] = item
  
  def create_jason_list(self, city):
    manager_data = JsonManager()
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

        aux.update({'country' : city[0]['country']})

        my_list.append(aux)

        j += 1
        
        auxiliar = jsonpath.jsonpath(self.items, "[0]")
        
    return my_list