# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:39:57 2022

@author: c1534096
"""

# given same output, should always return
# same output

# map, filter, zip, reduce
from functools import reduce

def multiply_by_2(li):
    #new_list = []

    return li*2
        
def only_odd(li):
    return li % 2 !=0

def accumalator(acc,item):
    print(acc,item)
    return acc + item
    
#print(multiply_by_2([1,2,3]))
y = [1,2,3]

x = reduce(accumalator,y,10) # map doesn't modify iterable
print(x)
print(y)