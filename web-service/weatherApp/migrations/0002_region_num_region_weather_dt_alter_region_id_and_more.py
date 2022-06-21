# Generated by Django 4.0.5 on 2022-06-21 16:37

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='num_region',
            field=models.CharField(default=django.utils.timezone.now, max_length=36),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weather',
            name='dt',
            field=models.CharField(default=django.utils.timezone.now, max_length=36),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
