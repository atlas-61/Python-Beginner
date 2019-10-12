# -*- coding: utf-8 -*-
import numpy as np

a = np.arange(10)
print(a)
b = a
a[0] = 100
print(a)
print(b)
print("* * * * ")
c = a.copy()
c[0] = 1000
print(a)
print(b)
print(c)
print("* * * * ")

d = a.view()
print(a)
print(d)
print("* * * * ")
d.shape = 2,5
print(a)
print(d)
print("* * * * ")

b.shape = 2,5
print(a)
print(b)