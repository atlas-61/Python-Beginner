# -*- coding: utf-8 -*-
import numpy as np

a = np.floor(10*np.random.random((3,5)))
print(a)
print("Shape: ", a.shape)
print(a.ravel()) #writes array as flat
a = a.ravel()
print(a)
print("Shape: ", a.shape)
print(a.reshape(2,9))
a = a.reshape(2,9)
print(a.T)# transpoze

print(a.reshape(-1,3)) # row*col must be equal number of elements
