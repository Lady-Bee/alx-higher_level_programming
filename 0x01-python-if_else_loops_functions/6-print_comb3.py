#!/usr/bin/python3
for first_digit in range(0, 8):
    for second_digit in range(0, 10):
        if not (second_digit <= first_digit):
            print("{:d}{:d}".format(first_digit, second_digit), end=", ")
print("89")
