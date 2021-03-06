# Generated by Django 4.0.5 on 2022-06-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('temp', models.CharField(max_length=8)),
                ('lat', models.CharField(max_length=10)),
                ('lon', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=150)),
                ('population', models.CharField(max_length=10)),
                ('timezone', models.CharField(max_length=10)),
                ('sunrise', models.CharField(max_length=10)),
                ('sunset', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
                'db_table': 'region',
                'ordering': ['-created_at'],
                'permissions': (('view_region', 'Can view region'),),
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('temp', models.CharField(max_length=8)),
                ('feels_like', models.CharField(max_length=8)),
                ('temp_min', models.CharField(max_length=8)),
                ('temp_max', models.CharField(max_length=8)),
                ('pressure', models.CharField(max_length=8)),
                ('humidity', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=8)),
                ('speed', models.CharField(max_length=8)),
                ('deg', models.CharField(max_length=8)),
                ('dt_txt', models.CharField(max_length=30)),
                ('region_id', models.CharField(max_length=36)),
                ('region', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=10)),
                ('lon', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=150)),
                ('population', models.CharField(max_length=10)),
                ('timezone', models.CharField(max_length=10)),
                ('sunrise', models.CharField(max_length=10)),
                ('sunset', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Weather',
                'verbose_name_plural': 'Weather',
                'db_table': 'weather',
                'ordering': ['-created_at'],
                'permissions': (('view_weather', 'Can view weather'),),
                'managed': True,
                'default_permissions': (),
            },
        ),
    ]
