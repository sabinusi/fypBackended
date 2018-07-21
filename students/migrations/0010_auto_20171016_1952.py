# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='proposed_supervisor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]