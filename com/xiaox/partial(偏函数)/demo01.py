#!/usr/bin/env python

# encoding: utf-8

"""
@author: xiaox

@contact: xiaoxgeek@163.com

@file: demo01.py

@time: 2018/1/18 16:14

@description:偏函数
"""
import functools
# 将字符串转化为数字，默认是十进制
print(int('12345'))
# 将字符串转化为数字，使用八进制
print(int('12345', base=8))


# 可以专门定义一个函数，默认使用八进制
def int8(args):
    return int(args, base=8)


print(int8('12345'))
# 可以使用偏函数来解决这个问题
int8 = functools.partial(int, base=8)
print(int8('12345'))