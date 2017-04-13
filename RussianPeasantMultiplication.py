# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:08:56 2017

@author: qiangwennorge
"""

def russianPeasantMultiplication(a,b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1: 
            z = z + y
        x = x >> 1
        y = y << 1
    return z    

print russianPeasantMultiplication(40,501)