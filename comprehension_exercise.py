# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:52:30 2022

@author: c1534096
"""

some_list = ['a','b','c','b','d','m','n','n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
            
print(duplicates)

dup = list({val for val in some_list if some_list.count(val) > 1 })

print(dup)


