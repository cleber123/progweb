# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-17 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0005_auto_20170517_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_rooms', to='pessoas.Discipline'),
        ),
    ]