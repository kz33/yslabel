# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-25 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpm', '0010_content_settings_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='classfy_list',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
