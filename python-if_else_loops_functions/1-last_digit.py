#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
<<<<<<< HEAD
if number > 0:
   digit = -digit
print("Last digit of {} is {} and is ".format(number, digit), end="")
=======
if number < 0:
    digit = -digit
print("Last digit of {} is {} and is "
      .format(number, digit), end="")
>>>>>>> 18367d374d3416e125ac6e29c481f3ad42693447
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
