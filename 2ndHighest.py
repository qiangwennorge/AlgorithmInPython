# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:52:08 2017

@author: qiangwennorge
"""

f = open('SourceInput/pop1995.txt','r')

maxname = "None"
maxage= 0
max2name = "None"
max2age = 0

for line in f:
    (name, sex, age) = line.rsplit(',')
    age = int(age)
    if sex == 'F':
        if age > maxage:
            max2name = maxname
            max2age = maxage
            maxname = name
            maxage = age
        elif age > max2age:
            max2name = name
            max2age = age
print maxname, maxage
print max2name, max2age