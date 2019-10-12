# -*- coding: utf-8 -*-
import random as rnd
row, column = 3, 3
# Matrix = [[0,0,0],[0,0,0],[0,0,0]]
Matrix = [[0 for x in range(column)] for y in range(row)] 
Matrix2 = [[0 for x in range(column)] for y in range(row)]

for r in range(0,row):
    for c in range(0,column):
        Matrix[r][c] = rnd.randint(1,10)
        Matrix2[r][c] = rnd.randint(1,10)

print(Matrix)
print(Matrix2)
        
SumMatrix = [[0 for x in range(column)] for y in range(row)]
for r in range(0,row):
    for c in range(0,column):
        SumMatrix[r][c] = Matrix[r][c] + Matrix2[r][c]
        
print(SumMatrix)

print(len(Matrix))