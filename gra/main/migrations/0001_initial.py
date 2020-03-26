# Generated by Django 2.2.5 on 2019-11-21 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_cat_title', models.CharField(max_length=200)),
                ('cat_summary', models.CharField(max_length=200)),
                ('cat_slug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]