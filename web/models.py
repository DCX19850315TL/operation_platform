# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class userinfo(models.Model):

    name = models.CharField(max_length=30)

    password = models.CharField(max_length=30)

    age = models.IntegerField()

    typeId = models.ForeignKey('usertype')

class usertype(models.Model):

    type = models.CharField(max_length=50)

class group(models.Model):

    Name = models.CharField(max_length=50)

class user(models.Model):

    Name = models.CharField(max_length=50)

    Email = models.CharField(max_length=50)

    group_relation = models.ManyToManyField('group')