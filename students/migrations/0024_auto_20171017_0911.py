# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 06:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_auto_20171016_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='students.StudentGroups'),
        ),
    ]
