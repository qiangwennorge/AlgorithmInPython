# -*- coding: utf-8 -*-
"""
Created on April 27 22:36 2017

@author: qiangwennorge
"""

'''
Stack() creates a new stack that is empty
push(item) adds a new item to the top of the stack
pop() removes the top item from the stack
peak() returns the top item from the stack but does not remove it
is_empty() tests to see whether the stack is empty
size() returns the number of items on the stack
'''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()

print s.is_empty()

s.push(4)

s.push('dog')

print s.peak()

s.push(True)

print s.size()

print s.is_empty()

s.push(8.4)

print s.pop()

print s.pop()

print s.size()