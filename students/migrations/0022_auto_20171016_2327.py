# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_auto_20171016_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group_number',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='students.StudentGroups'),
        ),
    ]
