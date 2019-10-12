# -*- coding: utf-8 -*-
setA = {1,2,3,4,5}  
setB = {1,3,4,6,7,8}
print (setA | setB) #union operation
print(setA.union(setB))

print(setA & setB) #intersection
print(setA.intersection(setB))

print(setA - setB) #difference 
print(setA.difference(setB))
print(setB.difference(setA))

print(setA ^ setB) # symmetric difference 
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))