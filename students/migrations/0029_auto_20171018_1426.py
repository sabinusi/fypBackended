# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0028_auto_20171018_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroups',
            name='first_member_reg_no',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='studentgroups',
            name='second_member_reg_no',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='studentgroups',
            name='third_member_reg_no',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
