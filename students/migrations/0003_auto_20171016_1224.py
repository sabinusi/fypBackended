# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20171016_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroupProjects',
            fields=[
                ('group_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='students.StudentGroups')),
                ('semister1_progress', models.FileField(blank=True, null=True, upload_to='Student_GroupsProject_Semister1_Progress/%Y/%m/%d')),
                ('semister1_final', models.FileField(blank=True, null=True, upload_to='Student_GroupsProject_Semister1_Final/%Y/%m/%d')),
                ('semister2_progress', models.FileField(blank=True, null=True, upload_to='Student_GroupsProject_Semister2_Progress/%Y/%m/%d')),
                ('semister2_Final', models.FileField(blank=True, null=True, upload_to='Student_GroupsProject_Semister2_Final/%Y/%m/%d')),
                ('title', models.TextField(null=True)),
                ('concept_note', models.FileField(blank=True, null=True, upload_to='Students_groups_projects_ConceptNotes/%Y/%m/%d')),
                ('semister1_progress_grades', models.IntegerField(default=0)),
                ('semister1_final_grades', models.IntegerField(default=0)),
                ('semister2_progress_grades', models.IntegerField(default=0)),
                ('semister2_Final_grades', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='group_number',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='students.StudentGroups'),
        ),
    ]