# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-01 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0021_auto_20171130_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='catequizando',
            name='is_activo',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catequizando',
            name='is_final',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
