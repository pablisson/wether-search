from django.contrib import admin
from weatherApp.models import Weather

class WeathersAdmin(admin.ModelAdmin):
    list_display = ('id', 'temp', 'feels_like', 'temp_min', 'temp_max', 'humidity', 'speed', 'city','lat', 'lon', 'country', 'population', 'timezone', 'sunrise', 'sunset', 'description')
    list_filter = ('id', 'temp', 'feels_like', 'temp_min', 'temp_max', 'humidity', 'speed', 'city', 'lat', 'lon', 'country', 'population', 'timezone', 'sunrise', 'sunset', 'description')
    search_fields = ( 'temp', 'feels_like', 'temp_min', 'temp_max', 'humidity', 'speed', 'city', 'lat', 'lon', 'country', 'population', 'timezone', 'sunrise', 'sunset', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10
    list_max_show_all = 10
    list_editable = ('temp', 'feels_like', 'temp_min', 'temp_max', 'humidity', 'speed', 'city', 'lat', 'lon', 'country', 'population', 'timezone', 'sunrise', 'sunset', 'description')
    list_per_page = 10
    list_max_show_all = 10
    

admin.site.register(Weather, WeathersAdmin)