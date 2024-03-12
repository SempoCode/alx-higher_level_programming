#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    lastDigit = (((number * -1) % 10) * -1)
else:
    lastDigit = number % 10

d = "Last digit of"
if (lastDigit > 5):
    print(f"{d} {number} is {lastDigit} and is greater than 5", end='\n')
elif (lastDigit == 0):
    print(f"{d} {number} is {lastDigit} and is 0", end='\n')
elif lastDigit < 6 and lastDigit != 0:
    s = "is less than 6 and not 0"
    print(f"{d} {number} is {lastDigit} and {s}", end='\n')
else:
    pass
