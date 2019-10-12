# -*- coding: utf-8 -*-
try:
    value = int(input("Enter a number: "))
except ValueError:  # also we can write type of the errors
    print("Invalid Value!")
