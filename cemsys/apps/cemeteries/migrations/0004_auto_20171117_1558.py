# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemeteries', '0003_auto_20171117_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
