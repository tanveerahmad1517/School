# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0014_auto_20171117_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnistudent',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
