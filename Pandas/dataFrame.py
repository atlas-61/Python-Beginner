# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)

data2 = [["Charles", 22, "Monaco"], ["Ryan", 54, "Rapture"],
         ["Karina", 39, "Kiev"]]
df2 = pd.DataFrame(data2, columns = ["Name", "Age", "Location"],
                   index = ["1.Person", "2.Person", "3.Person"])
print(df2)
print("* * * * *")
data3 = {
        "Name": ["Charles", "Ryan", "Karina"],
        "Age": [22, 54, 39],
        "Location": ["Monaco", "Rapture", "Kiev"]
        }
df3 = pd.DataFrame(data3)
print(df3)
print(df3["Name"])
#del df3["Location"]
#df3.pop("Location")
print(df3)
print("* * * * * ")
#print(df2.loc[1]) # in df2 no index named 1 but
print(df2.iloc[0]) # lines start with zero to n so name doesnt matter
df4 = df3.append(df2)
print(df4)
print("* * * * * ")
print(df4.iloc[4])
print(df4.head())
print(df4.tail())