# Generated by Django 2.2.5 on 2019-11-26 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_articleseries_mainarticle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleseries',
            old_name='series_title',
            new_name='article_series',
        ),
        migrations.AlterField(
            model_name='mainarticle',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 26, 4, 16, 29, 205492), verbose_name='date published'),
        ),
    ]
