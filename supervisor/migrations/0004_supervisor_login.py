# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0003_auto_20171016_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisor',
            name='login',
            field=models.BooleanField(default=False),
        ),
    ]