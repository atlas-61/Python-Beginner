# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1,3,5,7,9,11])
print(a.dtype)
print("Reshaped: \n", a.reshape(2,3))
print(a)
print("* * * * * *")
b = np.array([[1,3],[5,7],[9,11]])
print(b, b.ndim)