# Generated by Django 2.2.5 on 2019-12-07 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191205_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainarticle',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 8, 5, 13, 332009), verbose_name='date published'),
        ),
    ]
