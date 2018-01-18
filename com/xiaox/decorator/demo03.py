#!/usr/bin/env python

# encoding: utf-8

"""
@author: xiaox

@contact: xiaoxgeek@163.com

@file: demo03.py

@time: 2018/1/18 15:54

@description: 将原函数的前面也同步复制到装饰器中
"""
import time
from functools import reduce, wraps


def performance(unit):
    def decorator(f):
        @wraps(f)
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


print(factorial.__name__)