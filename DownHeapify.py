# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:05:51 2017

@author: qiangwennorge
"""

L = [50,88,27,58,30,21,58,13,84,24,29,43,61,44,65,74,76,30,82,42]

# Heap shortcuts
def left(i): 
    return i*2+1
def right(i):
    return i*2+2
def parent(i):
    return (i-1)/2
def root(i):
    return i == 0
def leaf(L,i):
    return right(i) >= len(L) and left(i) >= len(L)
def one_child(L,i):
    return right(i) == len(L)

# Call this routine if the heap rooted at i satisfies the heap propoertiy
# *except* perhaps i to its children immediate children
def down_heapify(L,i):
    # If i is a leaf, heap property holds
    if leaf(L,i): return
    # If i has one child 
    if one_child(L,i):
        # check heap property
        if L[i] > L[left(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (L[i],L[left(i)]) = (L[left(i)],L[i])
        return
    
    # If i has two children
    # check heap property
    if min(L[left(i)], L[right(i)]) >= L[i]:
        return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if L[left(i)] < L[right(i)]:
        # Swap into left child
        (L[i], L[left(i)]) = (L[left(i)],L[i])
    down_heapify(L,left(i))
    return
    (L[i],L[right(i)]) = (L[right(i)],L[i])
    down_heapify(L,right(i))
    return

print down_heapify(L,13)