from django.db import models
from uuid import uuid4

class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    num_region = models.CharField(max_length=36, null=True)
    name = models.CharField(max_length=200, null=True)
    temp = models.CharField(max_length=8, null=True)
    lat = models.CharField(max_length=10, null=True)
    lon = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=150, null=True)
    population = models.CharField(max_length=10, null=True)
    timezone = models.CharField(max_length=10, null=True)
    sunrise = models.CharField(max_length=10, null=True)
    sunset = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        ordering = ['-created_at']
        db_table = 'region'
        managed = True
        default_permissions = ()
        permissions = (
            ('view_region', 'Can view region'),
        )

class Weather(models.Model):
    #o id fará referncia ao campo dt
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    dt = models.CharField( max_length=36, null=True)    
    temp = models.CharField(max_length=8, null=True)
    feels_like = models.CharField(max_length=8, null=True)
    temp_min = models.CharField(max_length=8, null=True)
    temp_max = models.CharField(max_length=8, null=True)
    pressure = models.CharField(max_length=8, null=True)
    humidity = models.CharField(max_length=8, null=True)
    description = models.CharField(max_length=200, null=True)
    icon = models.CharField(max_length=8, null=True)
    speed = models.CharField(max_length=8, null=True)
    deg = models.CharField(max_length=8, null=True)
    dt_txt = models.CharField(max_length=30, null=True) 
    region_id = models.CharField(max_length=36, null=True)
    region = models.CharField(max_length=200, null=True) 
    lat = models.CharField(max_length=10, null=True)
    lon = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=150, null=True)
    population = models.CharField(max_length=10, null=True)
    timezone = models.CharField(max_length=10, null=True)
    sunrise = models.CharField(max_length=10, null=True)
    sunset = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Weather'
        verbose_name_plural = 'Weather'
        ordering = ['-created_at']
        db_table = 'weather'
        managed = True
        default_permissions = ()
        permissions = (
            ('view_weather', 'Can view weather'),
        )