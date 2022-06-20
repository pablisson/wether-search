from rest_framework import viewsets
from rest_framework.response import Response
from weatherApp.models import ClimaTempo, Cidade
from weatherApp.serializer import ClimaTempoSerializer, CidadeSerializer

from django.db.models import Q



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
    print(request.query_params.get('nome'))
    if request.query_params.get('nome') is not None:
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
      return Response(item.values('nome'))
    return Response(serializer.data)



 

  
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