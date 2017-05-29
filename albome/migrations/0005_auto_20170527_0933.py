# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-27 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albome', '0004_auto_20170527_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название'),
        ),
    ]
