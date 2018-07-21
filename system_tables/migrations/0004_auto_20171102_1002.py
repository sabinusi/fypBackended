# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_tables', '0003_systeamcontrol'),
    ]

    operations = [
        migrations.AddField(
            model_name='systeamcontrol',
            name='sem1final',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systeamcontrol',
            name='sem1progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systeamcontrol',
            name='sem2final',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systeamcontrol',
            name='sem2progress',
            field=models.BooleanField(default=False),
        ),
    ]