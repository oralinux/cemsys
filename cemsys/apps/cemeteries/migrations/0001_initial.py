# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grave_code', models.CharField(max_length=6)),
                ('grave_type', models.CharField(max_length=12)),
                ('grave_status', models.CharField(max_length=10)),
                ('grave_pic', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='TombArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tombarea_code', models.CharField(max_length=10)),
                ('tombarea_name', models.CharField(max_length=20)),
                ('remark', models.TextField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('operator', models.CharField(max_length=12)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('modify_operator', models.CharField(max_length=12)),
            ],
        ),
    ]
