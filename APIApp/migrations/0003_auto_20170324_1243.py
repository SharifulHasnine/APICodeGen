# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-24 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIApp', '0002_auto_20170324_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplecode',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]