# Generated by Django 2.2.5 on 2019-12-05 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191130_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainarticle',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 5, 2, 9, 30, 846802), verbose_name='date published'),
        ),
    ]
