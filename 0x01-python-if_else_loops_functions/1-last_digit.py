#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numberN = -1 * number
    lastdigit = numberN % 10
    lastdigit = -1 * lastdigit
else:
    lastdigit = number % 10


if lastdigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastdigit))
elif lastdigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastdigit))
else:
    print('Last digit of {} is {} and is less than 6 '
          'and not 0'.format(number, lastdigit))
