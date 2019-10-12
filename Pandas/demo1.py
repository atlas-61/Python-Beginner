# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

grades = pd.read_csv("grades.csv")
#print(grades)
#print(type(grades))
print(grades.head())
print(grades.tail())
print(grades["Last name"]) 
print("* * * * * *")
#print(grades["'First name'"]) column names have a problem we gonna fix
grades.columns = ["Last Name", "First Name",
               "SSN", "Test1", "Test2",
               "Test3", "Test4", "Final", "Grade"]
print(grades)
print(grades["Final"])
print(grades.iloc[5])
print(grades[0:5])

