# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0027_auto_20171018_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='students_profile_pictures/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentgroup',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='students.StudentGroups'),
        ),
    ]
