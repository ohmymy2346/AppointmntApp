# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointmentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='datetime',
            field=models.CharField(max_length=1000),
        ),
    ]
