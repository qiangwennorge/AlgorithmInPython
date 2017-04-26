# -*- coding: utf-8 -*-
"""
Created on April 26 19:39 2017

@author: qiangwennorge
"""

def reverse_str(s):
    if len(s) == 1:
        return s[0]
    else:
        return reverse_str(s[1:]) + s[0]

print reverse_str("alaska usa")

def is_palindrome(s):
    new_s = s.replace(' ','')
    re_s = reverse_str(new_s)
    if re_s == new_s:
        return True
    else:
        return False

print is_palindrome("live not on evil")