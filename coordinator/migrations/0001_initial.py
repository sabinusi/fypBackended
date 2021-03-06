# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('employee_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='cordinator_profile_pics')),
            ],
        ),
    ]
