# -*- coding: utf-8 -*-
numbers = [1,2,3,4,5]

#squareNum =[]
#for number in numbers:
#    squareNum.append(number*number)

squareNum = list(map(lambda number: number**2, numbers))

numbersFiltered = list(filter(lambda number: number > 2, numbers))

from functools import reduce
numbersFactorial = reduce(lambda x,y: x*y, numbers)
    
print(squareNum)
print(numbersFiltered)
print(numbersFactorial)
