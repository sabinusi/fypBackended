# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0029_auto_20171018_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroups',
            name='group_id',
            field=models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
    ]
