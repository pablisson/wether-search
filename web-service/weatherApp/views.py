from rest_framework import viewsets
from rest_framework.response import Response
from weatherApp.models import Weather, Region
from weatherApp.serializer import WeatherSerializer, RegionSerializer

from weatherApp.managerFileTransf.managerJson import ItemsForViewer



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
          viewer_list = ItemsForViewer()
          aux_values = viewer_list.create_jason_list(city)
          return Response(aux_values)
      else:
          viewer_list = ItemsForViewer()
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
    return Response(serializer.data)

  def list(self, request):
    queryset = self.filter_queryset(self.get_queryset())
    serializer = RegionSerializer(queryset, many=True)
    region = request.query_params.get('nome')
    print(request)
    if region is not None:    
      item = queryset.filter(name=request.query_params.get('nome'))
      if item.exists():
        viewer_list = ItemsForViewer()
        aux_values = viewer_list.create_jason_list(region)
        print(aux_values)
        return Response(item)
      else: 
        return Response([])
    return Response(serializer.data)

