# Generated by Django 5.1.5 on 2025-02-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodmanager', '0018_alter_reliefcamp_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('humidity', models.FloatField(blank=True, null=True)),
                ('wind_speed', models.FloatField(blank=True, null=True)),
                ('precipitation', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
