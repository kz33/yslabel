# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-06 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpm', '0014_content_group_settings_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='is_dirty_data',
            field=models.BooleanField(default=False),
        ),
    ]
