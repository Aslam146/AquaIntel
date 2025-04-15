# Generated by Django 5.1.5 on 2025-02-12 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodmanager', '0010_waterstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=100)),
                ('source_name', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('water_level', models.FloatField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('water_status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='floodmanager.waterstatus')),
            ],
        ),
    ]
