# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0013_remove_messagefromsudents_creted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagefromsudents',
            name='group_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]