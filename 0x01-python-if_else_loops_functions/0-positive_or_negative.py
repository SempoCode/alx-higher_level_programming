#!/usr/bin/python3
import random
number = random.randint(-10,10)
if (number > 0):
    print(f"{number} is postive", end='\n')
elif (number == 0):
    print(f"{number} is zero", end='\n')
else:
    print(f"{number} is negative", end='\n')
