# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-06 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20170905_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]