# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0040_auto_20171030_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='proposed_supervisor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='supervisor_employee_id',
        ),
        migrations.AddField(
            model_name='studentgroups',
            name='proposed_supervisor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentgroups',
            name='supervisor_employee_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]