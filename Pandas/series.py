# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = np.array(["Sandro", "Ricardo", "Jan"])
#s = pd.Series(data)
s = pd.Series(data, index=[1,2,3])
print(s)
data2 = {"math": 10, "physic": 20, "p.e.": 100}
s2 = pd.Series(data2)
print(s2)
print("* * * * * ")
s2 = pd.Series(data2, index=["physic", "p.e.", "math"]) #index names must be same as dict
print(s2)
s3 = pd.Series(5, index=[1,2,3,4,5,6])
print(s3)
print("* * * * * ")
print(s2[0])
print(s[1])
print(s2["math"])

