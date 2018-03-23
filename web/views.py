#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.shortcuts import HttpResponse
from web.models import userinfo,usertype

# Create your views here.
def index(request):

    return render_to_response('web/index.html')

def ops_page(request):

    return render_to_response('web/ops_page.html')
#增
def Add(request,type):

    usertype.objects.create(type=type)

    return HttpResponse('ok')
#删
def Delete(request,id):

    usertype.objects.get(id=id).delete()

    return HttpResponse('ok')
#改
def Update(request,id,type):
    '''
    #第一种写法
    obj = usertype.objects.get(id=id)
    obj.type = type
    obj.save()
    '''
    #第二种写法
    usertype.objects.filter(id__gt=id).update(type=type)
    return HttpResponse('ok')
#查
def Get(request,type):
    #模糊查询
    typelist = usertype.objects.filter(type__contains=type)

    for item in typelist:
        print item.type

    #取回所有数据
    alldata = usertype.objects.all()
    #打印原生的sql语句
    print alldata.query
    #只取出usertype表中的id字段的全部数据
    id = usertype.objects.all().values('id')
    print id
    print id.query

    #取所有数据的前两条
    temp = usertype.objects.all()[0:2]

    #以id正序排列
    usertype.objects.all().order_by('id')
    #以id倒序排列
    usertype.objects.all().order_by('-id')


    return HttpResponse('ok')
#把数据嵌套在html中，把这个html字符串返回给客户端
def all(request):

    all_list = usertype.objects.all()

    result = render_to_response('web/index.html',{'data':all_list,'user':'tanglei'})

    return result
