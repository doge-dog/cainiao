# -*- coding:utf-8 -*-
__author__ = 'winkin'
__date__ = '2017/8/29 17:32'

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello W orld!'
    context['user'] = 'Hello World!'
    context['currentuser'] = 'Hello W orld!'
    return render(request,'hello.html',context)