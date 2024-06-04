# Generated by Django 5.0.6 on 2024-06-04 20:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pm2_5', models.FloatField()),
                ('pm10', models.FloatField()),
                ('co2', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='sensors.sensor')),
            ],
        ),
    ]