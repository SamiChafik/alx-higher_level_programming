#!/usr/bin/python3
"""Print the numbers from 1 to 100 separated by a space.
For multiples of three, print Fizz instead of the number
For multiples of five, print Buzz instead of the number.
For multiples of three and five, print FizzBuzz instead of the number.
"""

for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
         if digit1 == 8 and digit2 == 9:
             print("{}{}".format(digit1, digit2))
         else:
             print("{}{}".format(digit1, digit2), end=", ")
