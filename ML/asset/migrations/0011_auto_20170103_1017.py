# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 02:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0010_auto_20170103_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4e8b\u4ef6\u6e90'),
        ),
    ]
