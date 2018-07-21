# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('conceptNote', models.FileField(upload_to='pastprojects/%y/%m/%d')),
                ('year', models.CharField(max_length=100)),
            ],
        ),
    ]