# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:39:57 2022

@author: c1534096
"""

# given same output, should always return
# same output

# map, filter, zip, reduce

def multiply_by_2(li):
    #new_list = []

    return li*2
        
def only_odd(li):
    return li % 2 !=0
 
    
#print(multiply_by_2([1,2,3]))
y = [1,2,3]
z = [10,20,30]
a = [5,4,3] # could be tuple, as log as it is iterable
x = list(zip(y,z,a)) # map doesn't modify iterable
print(x)
print(y)