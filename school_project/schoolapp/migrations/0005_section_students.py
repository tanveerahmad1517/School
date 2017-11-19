# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_auto_20171113_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionclass', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.IntegerField()),
                ('division', models.CharField(max_length=20)),
                ('attendence', models.IntegerField()),
                ('quaterly_exam', models.IntegerField()),
                ('half_yearly', models.IntegerField()),
                ('annual', models.IntegerField()),
                ('contact_no', models.IntegerField()),
                ('address', models.TextField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='schoolapp.Section')),
            ],
        ),
    ]