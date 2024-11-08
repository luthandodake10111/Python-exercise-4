#Question 1: Using a for loop with a list
from random import random
from warnings import simplefilter

from list import colors

for fruit in range(1,6):
    print(fruit)


fruit= ["banana","naaitjie", "apple", "kiwi", "orange"]
for fruit in list(fruit):
    print(fruit)

#__________________________________________________________________________
#Question 2: Using a while loop for countdown
count = 10
while count > 0:
    print(count)
    count -= 1

count= 15
while count >5:
    print(count)
    count -= 1

#_________________________________________________________________________
#Question 3: Using a for loop with range()
for square_numbers in range(1, 10, 2):
    print(square_numbers)

#_________________________________________________________________________
#Question 4: Using the random module

import random
list_color= ["Black","Green","Yellow","Blue","Pink"]

random_color= random.sample(list_color,3)

for list_color in random_color:
    print(list_color)

#_________________________________________________________________________
#Question 5: Creating and using a custom module
import math_operation
print(math_operation.add(5, 5))
print(math_operation.divide(7, 1))
print(math_operation.multiply(8, 5))
print(math_operation.subtract(50,40))


def simple_calculator():
    print("correct")
    print("incorrect")

