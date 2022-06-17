# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:46:11 2022

@author: c1534096
"""

my_list = {char for char in 'hello'}
#print(my_list)

simple_dict = {'a':1,
               'b':2}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
print(my_dict)

my_dict_2 = {num:num**2 for num in [1,2,3]}

print(my_dict_2)