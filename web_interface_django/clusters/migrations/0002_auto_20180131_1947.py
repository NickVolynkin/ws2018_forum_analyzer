# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster',
            name='name',
        ),
        migrations.AddField(
            model_name='cluster',
            name='summary',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]