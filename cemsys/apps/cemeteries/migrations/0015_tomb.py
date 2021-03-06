# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemeteries', '0014_auto_20171123_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tomb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.CharField(max_length=10)),
                ('area_name', models.CharField(max_length=20)),
                ('cate_code', models.CharField(max_length=10)),
                ('cate_name', models.CharField(max_length=20)),
                ('cate_type', models.CharField(max_length=4)),
                ('grave_status', models.CharField(max_length=10)),
                ('tomb_row', models.CharField(max_length=4)),
                ('tomb_col', models.CharField(max_length=4)),
                ('tomb_attach', models.CharField(default=0, max_length=4)),
                ('area', models.FloatField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('operator', models.CharField(max_length=12)),
            ],
        ),
    ]
