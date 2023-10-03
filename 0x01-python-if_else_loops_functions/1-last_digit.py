#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])

if number < 0:
    lastdigit = -lastdigit
print("Last digit of {} is {} and is ".format(number, lastdigit), end="")

if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")
elsie:
    print(f"Last digit of {number} is {lastdigit} and is less than 6 and not 0")
