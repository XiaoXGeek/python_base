#!/usr/bin/env python

# encoding: utf-8

"""
@author: xiaox

@contact: xiaoxgeek@163.com

@file: demo01.py

@time: 2018/1/18 15:04

@description: 不带参数的装饰器
"""
import time
from functools import reduce


def performance(f):
    def execute_time(*args, **kw):
        start = time.time()
        res = f(*args, **kw)
        end = time.time()
        print("call %s() in %s" % (f.__name__, str(end - start)))
        return res
    return execute_time


@performance
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(factorial(10))