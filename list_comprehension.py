# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:39:53 2022

@author: c1534096
"""

# list, set, dictionary

my_list = [char for char in 'hello']
print(my_list)

my_list2 = [2*num for num in range(100)]
print(my_list2)

my_list3 = [num**2 for num in range(100)
if num%2 ==0]
print(my_list3)