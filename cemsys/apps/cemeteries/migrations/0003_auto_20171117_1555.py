# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemeteries', '0002_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grave',
            name='grave_pic',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]