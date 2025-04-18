# Generated by Django 5.1.5 on 2025-02-12 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodmanager', '0026_emergencysupply'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvacuationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people_evacuated', models.IntegerField()),
                ('evacuation_center', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=15)),
                ('emergency_supply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floodmanager.emergencysupply')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floodmanager.evacuationlocation')),
                ('transport_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floodmanager.transportmethod')),
            ],
        ),
    ]
