# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0016_auto_20171119_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catequista',
            name='id_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inscripcion.Area'),
        ),
    ]