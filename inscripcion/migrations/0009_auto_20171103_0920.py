# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-03 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0008_auto_20171103_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleta',
            name='id_area',
        ),
        migrations.RemoveField(
            model_name='boleta',
            name='id_catequista',
        ),
        migrations.RemoveField(
            model_name='boleta',
            name='id_catequizando',
        ),
        migrations.RemoveField(
            model_name='boleta',
            name='id_comunidad',
        ),
        migrations.DeleteModel(
            name='Boleta',
        ),
        migrations.DeleteModel(
            name='Catequista',
        ),
    ]