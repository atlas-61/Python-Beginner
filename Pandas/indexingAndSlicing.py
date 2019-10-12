# -*- coding: utf-8 -*-
import pandas as pd
grades = pd.read_csv("grades.csv")
grades.columns = ["Last Name", "First Name",
               "SSN", "Test1", "Test2",
               "Test3", "Test4", "Final", "Grade"]
print(grades.loc[::-1, "First Name"]) # all rows one columns
test = grades.loc[:5, "First Name": "Final"]
print(test)
print("* * * * * ")
print(grades.loc[:5, ["First Name" , "Final"]] ) # first name and final