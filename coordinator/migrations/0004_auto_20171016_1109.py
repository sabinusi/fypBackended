# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinator', '0003_coordinatoranaucements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinatoranaucements',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
