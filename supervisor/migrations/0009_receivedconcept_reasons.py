# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0008_auto_20171118_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivedconcept',
            name='reasons',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
