# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0010_auto_20171119_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagefromsudents',
            name='creted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
