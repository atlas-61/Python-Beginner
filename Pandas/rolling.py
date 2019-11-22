# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
df = pd.DataFrame({"Col": [0,1,2,3,4,np.nan,6,7,8,9,10]})
print(df.rolling(2).sum())
print("* * * * * * * ")
print(df.rolling(2, min_periods = 1).sum())
