# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:39:57 2022

@author: c1534096
"""
from functools import reduce

# lambda expressions


# lambda param: action(param)
        
def only_odd(li):
    return li % 2 !=0
 
def accumalator(acc,item):
    print(acc,item)
    return acc + item
   
#print(multiply_by_2([1,2,3]))
a = [1,2,3]
z = [10,20,30]

# lambda param: action(param)
x = list(map(lambda item:item*2,z))
y = list(map(lambda item:item %2 !=0,a))
b = reduce(lambda acc,item:acc+item,a)

 # could be tuple, as log as it is iterable
#x = list(zip(y,z,a)) # map doesn't modify iterable
print(x)
print(y)
print(b)