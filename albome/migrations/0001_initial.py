# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-23 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='название')),
                ('image', models.ImageField(upload_to='albome/photos', verbose_name='изображение')),
                ('date', models.DateTimeField()),
                ('slug', models.SlugField(max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='albome/photos', verbose_name='изображение')),
                ('title', models.CharField(blank=True, default='', max_length=255, verbose_name='название')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='albome.Album', verbose_name='альбом')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['title'],
            },
        ),
    ]