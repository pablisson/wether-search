from django.contrib import admin
from django.urls import path, include
from weatherApp.views import WeatherViewSet, RegionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'weather', WeatherViewSet, basename='weather')
router.register(r'region', RegionViewSet, basename='region')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
