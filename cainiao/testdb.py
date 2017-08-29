# -*- coding:utf-8 -*-
__author__ = 'winkin'
__date__ = '2017/8/29 19:56'

from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse('<h1>save data sucussyful</h1>')