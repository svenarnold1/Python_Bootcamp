# Day 9 in python bootcamp

# wall paint calculator
from math import ceil
test_h = float(input('input the height wall: '))
test_w = float(input('input the with of wall: '))
# 1 can of paint covers 5 square meters of the wall!
coverage = 5


def paint_calc(height, width, cover):
    area = height * width
    num_of_can = ceil(area / cover)
    return f"You'll need {num_of_can} cans of paint"


print(paint_calc(height=test_h, width=test_w, cover=coverage))

# prime number checker


def prime_checker(number):
    if number == 1:
        return "it's a prime number."
    else:
        for i in range(2, number):
            if number % i != 0:
                return "it's a prime number."
            else:
                return "It's not a prime number."


num = int(input('input a number you want to check: '))

print(prime_checker(num))

