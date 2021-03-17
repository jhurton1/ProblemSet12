# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 08:09:59 2021

@author: Student
"""
#Jack Hurton
#Problem Set 5
#Feb 4th, 2021


import random
min = 1
max = 6

number_of_rolls = int(input("How many times would you like to roll the dice? "))
count = number_of_rolls

twos = 0
threes = 0
fours = 0
fives = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

while number_of_rolls >= count and count > 0:
    print("Rolling the dices")
    print("The values are: ...")
    print (random.randint(min, max))
    print (random.randint(min, max))
    count = count -1
    
