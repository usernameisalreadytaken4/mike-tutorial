# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-08 17:21
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='default_title', max_length=100)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=0, verbose_name='date published')),
                ('likes', models.IntegerField(default=0)),
                ('thumbnail', models.FileField(default='default.png', upload_to=articles.models.get_upload_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('second_name', models.CharField(default='', max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=0, verbose_name='date published')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]
