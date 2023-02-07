#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 19:48:56 2023

M2C3 Python assignment
"""

# Exercise 1
name = 'Katrine'
age = 25
list_of_courses = ['Python', 'JavaScrpit', 'React']
is_finished = False


# Exercise 2
first_letters = name[0:3]


# Exercise 3
first_element = list_of_courses[0]


# Exercise 4
added_age = age + 10


# Exercise 5 
last_element = first_element = list_of_courses[-1]


# Exercise 6
names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(',')


# Exercise 7
cap_name = names[0:5].upper()

    # form1
new_names = names.replace(names[0:5], cap_name)
    # form2
new_names_2 = cap_name + names[5:]


# Exercise 8
print(f'{name} is {age} years old')

# Exercise 9
print('hello wordl')