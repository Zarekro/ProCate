# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-03 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catequista',
            fields=[
                ('id_catequista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('usename', models.CharField(max_length=12)),
                ('contra', models.CharField(max_length=20)),
            ],
        ),
    ]