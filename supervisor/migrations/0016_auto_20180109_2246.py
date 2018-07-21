# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-09 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0015_auto_20180109_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='panel',
            name='eight_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panel',
            name='fifth_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panel',
            name='fourth_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panel',
            name='nine_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panel',
            name='second_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panel',
            name='seven_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panel',
            name='six_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panel',
            name='ten_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panel',
            name='third_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='eight_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='fifth_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='first_groupid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='first_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='fourth_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='second_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='seven_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='six_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='third_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]