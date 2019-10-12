# -*- coding: utf-8 -*-
import pandas as pd

orders = pd.read_table("orders.tsv")
print(orders.head())
print(orders.columns)
orders.item_name = orders.item_name.str.upper()
print(orders.head())
print(orders.item_name.str.contains("CHICKEN"))
orders.choice_description = orders.choice_description.str.replace("[","").str.replace("]","")
