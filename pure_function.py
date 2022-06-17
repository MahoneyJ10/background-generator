# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:39:57 2022

@author: c1534096
"""

# given same output, should always return
# same output

# map, filter, zip, reduce

def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(2*item)
    return new_list
        

#print(multiply_by_2([1,2,3]))

x = list(map(multiply_by_2,[1,2,3]))
