# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 03:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpm', '0005_auto_20171211_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='key1_positions',
            new_name='key_positions',
        ),
        migrations.RemoveField(
            model_name='content',
            name='key2_positions',
        ),
    ]
