# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0054_messagefromcoordinator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='students.StudentGroups'),
        ),
    ]
