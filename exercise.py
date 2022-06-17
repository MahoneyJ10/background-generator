# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:48:29 2022

@author: c1534096
"""

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def caps(li):
    #new_list = []

    return li.capitalize()

x = list(map(caps,my_pets))
print(x)
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
#my_numbers = [5,4,3,2,1]
my_numbers.sort()
def ascend(li):
    x = li.sort()
    return x

new_list = list(zip(my_strings,sorted(my_numbers)))
print(new_list)
#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def over_50(li):
    return li > 50

 
#print(multiply_by_2([1,2,3]))
x = list(filter(over_50,scores))
print(x)

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumalator(acc,item):
    print(acc,item)
    return acc + item
#y = reduce(accumalator,scores,0)
x = reduce(accumalator,my_numbers+scores,0) # map doesn't modify iterable
print(x)
