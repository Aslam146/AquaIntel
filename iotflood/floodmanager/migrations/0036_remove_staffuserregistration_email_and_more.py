# Generated by Django 5.1.5 on 2025-02-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floodmanager', '0035_staffuserregistration_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffuserregistration',
            name='Email',
        ),
        migrations.AddField(
            model_name='staffuserregistration',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
