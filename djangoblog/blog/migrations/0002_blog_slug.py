# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-06 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]