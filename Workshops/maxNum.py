# -*- coding: utf-8 -*-
value = int(input("First num:"))
temp = int(input("Second num:"))
if temp > value:
    value = temp
temp = int(input("Third num:"))
if temp > value:
    value = temp
    
print("Max num:",value)
