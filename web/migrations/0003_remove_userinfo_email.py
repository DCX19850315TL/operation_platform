# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 03:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_userinfo_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
    ]
