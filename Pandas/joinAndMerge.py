# -*- coding: utf-8 -*-
import pandas as pd

data1 = {
        "id": [1,2,3,4],
        "name": ["Karina", "Elena", "Walter", "Gustavo"],
        "surname": ["Play", "Koshka", "White", "Fring"]
        }
data2 = {
        "id": [1,3,4,7],
        "name": ["Jacub", "Marcus", "Dani", "Anita"],
        "surname": ["Mackovic", "Wasser", "Azur", "Kusnetsova"]
        }

data_df1 = pd.DataFrame(data1)
data_df2 = pd.DataFrame(data2)
print(data_df1)
print(data_df2)

print(pd.merge(data_df1, data_df2, on = "id", how = "inner"))
print(pd.merge(data_df1, data_df2, on = "id", how = "left"))
print(pd.merge(data_df1, data_df2, on = "id", how = "right"))

print(pd.concat([data_df1, data_df2]))
print(pd.concat([data_df1, data_df2], axis = 1))
