# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-19 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_blog_blog_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reple',
            name='user',
        ),
        migrations.DeleteModel(
            name='Reple',
        ),
    ]