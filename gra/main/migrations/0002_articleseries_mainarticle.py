# Generated by Django 2.2.5 on 2019-11-22 05:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_title', models.CharField(max_length=200)),
                ('series_summary', models.CharField(max_length=200)),
                ('main_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.MainCategory', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='MainArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_content', models.TextField()),
                ('date_published', models.DateTimeField(default=datetime.datetime(2019, 11, 22, 5, 28, 7, 182621), verbose_name='date published')),
                ('article_slug', models.CharField(default=1, max_length=200)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('article_series', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.ArticleSeries', verbose_name='Series')),
            ],
        ),
    ]