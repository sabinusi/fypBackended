# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinator',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='cordinator_profile_pics'),
        ),
    ]
