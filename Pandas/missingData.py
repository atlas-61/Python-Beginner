# -*- coding: utf-8 -*-
import pandas as pd

#url = "https://bit.ly/35lWqai"
#data = pd.read_csv(url)
#print(data)
# it works but slow

data = pd.read_csv("ufo.csv")
#print(data)
print(data.columns)
print(data.isnull().head(100))
print(data.notnull().head(100))
print(data.isnull().sum())
print(data[data.City.isnull()]) #shows all NaN cities
print("* * * * *")
print(data.shape)

#data = data.dropna() #deletes all NaN values
#data = data.dropna(how = "all") #if all line empty it deletes
#data = data.dropna(subset = ["City"], how = "all")
print(data["Shape Reported"].value_counts(dropna = False))
print(data.shape)
data["Shape Reported"].fillna(value = "UNCLEAR", inplace = True)
print(data["Shape Reported"].value_counts(dropna = False))