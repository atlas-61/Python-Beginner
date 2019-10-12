# -*- coding: utf-8 -*-
import numpy as np
numbers = np.array([0,5,10,15,20,25,30])

print(numbers[0])
print(numbers[::-1])
#print(numbers[0:3])

numbers2 = np.array([[0,5,10],[15,20,25]])
print(numbers2[1][2])
print(numbers2[:, 2]) #all rows third column
print(numbers2[-1, :])
print(numbers2[:, -1], "*")


    