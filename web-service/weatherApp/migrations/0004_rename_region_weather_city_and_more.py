# Generated by Django 4.0.5 on 2022-06-21 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0003_alter_region_country_alter_region_lat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='region',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='weather',
            old_name='region_id',
            new_name='city_id',
        ),
    ]