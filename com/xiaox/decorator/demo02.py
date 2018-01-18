#!/usr/bin/env python

# encoding: utf-8

"""
@author: xiaox

@contact: xiaoxgeek@163.com

@file: demo02.py

@time: 2018/1/18 15:33

@description: 带参数的装饰器
打印函数执行时间
"""
import time
from functools import reduce


def performance(unit):
    def decorator(f):
        def execute_time(*args, **kw):
            start = time.time()
            res = f(*args, **kw)
            end = time.time()
            use_time = end - start
            if 's' == unit:
                use_time = 1000 * use_time
            print("[%s]call %s() in %s" % (unit, f.__name__, use_time))
            return res
        return execute_time
    return decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print(factorial(10))