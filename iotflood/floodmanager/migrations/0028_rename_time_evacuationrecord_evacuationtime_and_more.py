# Generated by Django 5.1.5 on 2025-02-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodmanager', '0027_evacuationrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evacuationrecord',
            old_name='time',
            new_name='evacuationtime',
        ),
        migrations.AlterField(
            model_name='transportmethod',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
