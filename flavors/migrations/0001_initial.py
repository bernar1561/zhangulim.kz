# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-23 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='flavors/photos', verbose_name='изображение')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('description', models.TextField(verbose_name='описание')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Букет',
                'verbose_name_plural': 'Букеты',
                'ordering': ['title'],
            },
        ),
    ]