# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-10 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170410_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='timeout',
        ),
        migrations.AlterField(
            model_name='chat',
            name='expiration_time',
            field=models.FloatField(default=1491859136.456045),
        ),
    ]
