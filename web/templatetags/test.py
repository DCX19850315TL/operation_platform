#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: test.py
@time: 2017/11/29 17:19
'''
from django import template
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

@register.simple_tag
def mymethod(v1):
    result = v1*1000
    return result