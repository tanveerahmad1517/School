# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0012_alumni_alumnistudent_sendrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='year',
            field=models.IntegerField(),
        ),
    ]