# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-02 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0018_auto_20171202_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acheiver',
            name='image',
        ),
        migrations.RemoveField(
            model_name='alumnistudent',
            name='image',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='image',
        ),
        migrations.RemoveField(
            model_name='gallary',
            name='image',
        ),
        migrations.RemoveField(
            model_name='students',
            name='image',
        ),
    ]
