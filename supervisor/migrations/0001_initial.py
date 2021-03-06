# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import supervisor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, verbose_name=supervisor.models.Supervisor)),
                ('student_title', models.TextField()),
                ('message_from_student', models.TextField()),
                ('student_names', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField(default=0)),
                ('experties', models.CharField(max_length=500)),
                ('ofice_number', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='supervisors_profile_pics/%Y/%m/%d')),
            ],
        ),
    ]
