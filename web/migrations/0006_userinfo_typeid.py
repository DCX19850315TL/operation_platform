# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 04:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='typeId',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='web.usertype'),
            preserve_default=False,
        ),
    ]
