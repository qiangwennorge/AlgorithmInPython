# -*- coding: utf-8 -*-
"""
Created on April 26 19:29 2017

@author: qiangwennorge
"""

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n / base, base) + convert_string[n % base]

print(to_str(1453, 16))