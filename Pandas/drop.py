# -*- coding: utf-8 -*-
import pandas as pd

films = pd.read_csv("imdb-1000.csv")
print(films.columns)
print(films.drop("content_rating", axis = 1).head())# deletes col if axis = 1, axis = 0 means line

test = films.drop("content_rating", axis = 1)
print(test.columns)
films.drop(2, axis= 0) #deletes second row

rowsToDrop = [0,1,2,4,6,8,9,10]
test = test.drop(rowsToDrop, axis = 0)
print(test)
print(test.mean())