#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = -1990
if number < 0:
    if number % 10 == 0:
        print(f"{number} last digit is {number % -10} and is 0")
    elif number % -10 < 6 and number % -10 != 0:
        print(f"{number} last digit is {number % -10} and is less than 6 and not 0")
    else:
        print(f"{number} last digit is {number % -10 * -1}")

elif number > 0:
    
    if number % 10 > 5:
        print(f"{number} last digit is {number % 10} and is greater than 5")
    elif number % 10 < 6 and number % 10 != 0:
        print(f"{number} last digit is {number % 10} and is less than 6 and not 0")
    else: 
        print(f"{number} last digit is {number % 10} and is 0")
