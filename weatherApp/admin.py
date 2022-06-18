from django.contrib import admin
from weatherApp.models import ClimaTempo

class ClimaTemposAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'temperatura', 'pressao', 'humidade', 'vento', 'umidade', 'descricao', 'icon', 'cidade', 'estado', 'pais', 'latitude', 'longitude')
    list_filter = ('data', 'temperatura', 'pressao', 'humidade', 'vento', 'umidade', 'descricao', 'icon', 'cidade', 'estado', 'pais', 'latitude', 'longitude')
    search_fields = ('id','data', 'temperatura', 'pressao', 'humidade', 'vento', 'umidade', 'descricao', 'icon', 'cidade', 'estado', 'pais', 'latitude', 'longitude')
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 10
    list_max_show_all = 10
    list_editable = ('temperatura', 'pressao', 'humidade', 'vento', 'umidade', 'descricao', 'icon', 'cidade', 'estado', 'pais', 'latitude', 'longitude')
    #list_display_links = ('id','descricao', 'cidade', 'estado', 'pais')
    #list_select_related = ('data', 'temperatura', 'pressao', 'humidade', 'vento', 'umidade', 'descricao', 'icon', 'cidade', 'estado', 'pais', 'latitude', 'longitude')
    list_per_page = 10
    list_max_show_all = 10
    list_editable = ('temperatura', 'pressao', 'humidade', 'vento', 'umidade', 'descricao', 'icon', 'cidade', 'estado', 'pais', 'latitude', 'longitude')

admin.site.register(ClimaTempo, ClimaTemposAdmin)