# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-19 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_buddy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/post'),
        ),
    ]
