# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0041_auto_20171030_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroups',
            name='proposed_supervisor',
            field=models.CharField(max_length=100),
        ),
    ]
