# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0033_auto_20171018_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='role',
            field=models.CharField(default='student', max_length=20),
        ),
    ]
