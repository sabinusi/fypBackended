# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinator', '0008_coordinator_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinator',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
