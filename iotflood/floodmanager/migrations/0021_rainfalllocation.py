# Generated by Django 5.1.5 on 2025-02-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodmanager', '0020_remove_weather_precipitation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RainfallLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
