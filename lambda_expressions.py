# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:23:25 2022

@author: c1534096
"""

my_list = [5,4,3]

x = list(map(lambda item:item**2,my_list))
#print(x)

a = [(0,2),(4,3),(9,9),(10,-1)]
# would work with dictionaries too!
a.sort(key = lambda item:item[1])
print(a)
