# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-03 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0004_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catequista',
            name='usename',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
