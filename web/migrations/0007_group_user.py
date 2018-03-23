# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_userinfo_typeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('group_relation', models.ManyToManyField(to='web.group')),
            ],
        ),
    ]