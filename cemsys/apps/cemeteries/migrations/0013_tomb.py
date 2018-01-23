# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cemeteries', '0012_cate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tomb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tomb_row', models.CharField(max_length=4)),
                ('tomb_col', models.CharField(max_length=4)),
                ('tomb_attach', models.CharField(max_length=4)),
                ('tomb_sign', models.CharField(default='', max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('operator', models.CharField(max_length=12)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemeteries.Area')),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemeteries.Cate')),
                ('grave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cemeteries.Grave')),
            ],
        ),
    ]