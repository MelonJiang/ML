# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-01 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20170101_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='module',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u6a21\u5757'),
        ),
    ]
