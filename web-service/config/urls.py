"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from weatherApp.views import WeatherViewSet, RegionViewSet, UpdateDeletePostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'weather', WeatherViewSet, basename='weather')
router.register(r'region', RegionViewSet, basename='region')
#router.register(r'delete/<int:pk>', UpdateDeletePostViewSet.as_view(), basename='delete')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('delete/<int:pk>', UpdateDeletePostViewSet.as_view())
    #path('post/<int:pk>', UpdateDeletePostViewSet()),
]
