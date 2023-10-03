#!/usr/bin/python3
for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        print(f"{first_digit}{second_digit:02d}", end=', ' if first_digit < 8 else ',\n')
