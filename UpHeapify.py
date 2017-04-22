# -*- coding: utf-8 -*-
"""
Created on April 22 17:15 2017

@author: qiangwennorge
"""

def parent(i):
    return (i-1)/2
def left_child(i):
    return 2*i+1
def right_child(i):
    return 2*i+2
def is_leaf(L,i):
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i):
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def up_heapify(L, i):
    while L[i] < L[parent(i)] and i > 0:
        (L[parent(i)],L[i]) = (L[i],L[parent(i)])
        i = parent(i)
    print L
    return

L = [2, 4, 3, 5, 9, 7, 7]
L.append(1)

up_heapify(L,7)