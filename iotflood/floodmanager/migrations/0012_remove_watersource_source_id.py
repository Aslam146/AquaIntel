# Generated by Django 5.1.5 on 2025-02-12 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floodmanager', '0011_watersource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watersource',
            name='source_id',
        ),
    ]
