# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0055_auto_20171122_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentgroup',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='students.StudentGroups'),
        ),
    ]