# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemeteries', '0005_auto_20171117_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.FileField(upload_to='images'),
        ),
    ]
