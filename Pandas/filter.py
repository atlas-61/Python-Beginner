# -*- coding: utf-8 -*-
import pandas as pd
films = pd.read_csv("imdb-1000.csv")
print(films.columns)
print(films.loc[:5, :"title"])
print("* * * * * *")
print(films["title"].head())
print(films.title.head()) # same as line 7
print("* * * * * *")

print(films[["title", "star_rating"]].head())
print(films[:9][["title", "star_rating"]])
print(films[films["star_rating"]>8.5][["title", "star_rating"]])

print(films[(films["star_rating"]>8.5) & (films["star_rating"]<9.0)][["title", "star_rating"]])
print("* * * * * *")
print(films.query("star_rating >= 9.0")[["title", "star_rating"]])
        

