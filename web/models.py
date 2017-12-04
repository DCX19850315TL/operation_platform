# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class userinfo(models.Model):

    name = models.CharField(max_length=30)

    password = models.CharField(max_length=30)

    age = models.IntegerField()

class usertype(models.Model):

    type = models.CharField(max_length=50)