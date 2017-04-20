# -*- coding: utf-8 -*-
"""
Created on Thur Apr 20 21:29:51 2017

Running Time: Big Theta(n*log n)

@author: qiangwennorge
"""
#
# Implement remove_min[]
def remove_min(L):
    # remove last element, and replace first element with it
    L[0] = L.pop()
    # run down_heapify on the first element to maintain the heap property
    down_heapify(L,0)
    return L

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

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its immediate children
def down_heapify(L, i):
    # If i is a leaf, heap property holds
    if is_leaf(L, i):
        return
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if L[i] > L[left_child(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        return
    # If i has two children...
    # check heap property
    if min(L[left_child(i)], L[right_child(i)]) >= L[i]:
        return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if L[left_child(i)] < L[right_child(i)]:
        # Swap into left child
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        down_heapify(L, left_child(i))
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        down_heapify(L, right_child(i))
        return

#########
# Testing Code
#########

# build_heap
def build_heap(L):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
    return L


# fetch min and remove min and then down heapify
def heap_sorting(L, res = []):
    if len(L) <= 1:
        res.extend(L)
    else:
        res.append(L[0])
        remove_min(L)
        heap_sorting(L,res)
    return res


def test():
    L = [1,2,5,3,6,9,4,7,8,0]
    #L = range(10)
    build_heap(L)
    print heap_sorting(L)

test()
