# Generated by Django 5.1.5 on 2025-03-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodmanager', '0038_remove_rainfallintensity_rainfall_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloodAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_msg', models.TextField()),
                ('landscape_level', models.CharField(choices=[('high', 'High'), ('moderate', 'Moderate'), ('low', 'Low')], max_length=10)),
                ('route', models.TextField()),
                ('alert_date', models.DateField()),
            ],
        ),
    ]
