# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 23:04:02 2017

@author: qiangwennorge
"""

def binarySearch (array, left, right, target):
    # Sort the array
    array.sort()
    if right >= left:
        mid = left + (right -1) / 2
        # If the element is present at the middle
        if array[mid] == target:
            return mid
        # If the element is smaller than the middle item, then it should be in the left subarray
        elif array[mid] > target:
            return binarySearch(array, left, mid - 1, target)
        # If the element is large than the middle item, then it should be in the right subarray
        else:
            return binarySearch(array, mid + 1, right, target)
            
    else:
        # If the element is not in the array
        return -1
 
 # Test
array = [1,2,3,4,5,6,7,8,9]
target = 3

result = binarySearch(array, 0, len(array) - 1, target)

if result is not -1:
    print "Element is found at index %d" % result
else:
    print "Element is not found in the array"

