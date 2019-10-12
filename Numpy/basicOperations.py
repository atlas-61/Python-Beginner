# -*- coding: utf-8 -*-
import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)
c = a -b
d = a**3
e = 10 * np.sin(a)
f = e < 7
print(f)
print(a*b)
print(a@b) #matrix product
print(a.dot(b))

m = np.zeros((3,3))
n = np.ones((3,3))
r = np.random.random((3,3)) # range 0 < r < 1
i = np.sum(b)
j, k = np.max(b), np.min(b)
l = np.sqrt(b)


print(m, "\n", n, "\n", r, "\n", i)
print(j, k, l)