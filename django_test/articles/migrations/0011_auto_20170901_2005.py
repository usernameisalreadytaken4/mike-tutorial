# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 20:05
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20170901_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default='media/default.png', upload_to=articles.models.get_upload_file_name),
        ),
    ]
