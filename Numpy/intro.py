# -*- coding: utf-8 -*-
import numpy as np
weatherForecast= [30,25,28,27,20,22,23,20,24,18,20,23,21,20,19,17,18]
print(weatherForecast)

a = np.arange(15).reshape(3,5)
print(a)
print(type(a))

b = np.arange(10)
print(a.shape, a.ndim)
print(b.shape, b.ndim)