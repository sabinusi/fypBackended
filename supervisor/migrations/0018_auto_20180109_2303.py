# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-09 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0017_auto_20180109_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='panel_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
