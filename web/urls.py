#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: urls.py
@time: 2017/11/29 10:54
'''
from django.conf.urls import url
from web.views import index,ops_page,Add,Delete,Update,Get,all

urlpatterns = [
    url(r'^index/$',index),
    url(r'^ops_page/$',ops_page),
    url(r'^add/(?P<type>\w*)/$',Add),
    url(r'^delete/(?P<id>\d*)/$',Delete),
    url(r'^update/(?P<id>\d*)/(?P<type>\w*)/$',Update),
    url(r'^get/(?P<type>\w*)/$',Get),
    url(r'^all/$',all),
]