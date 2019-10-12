# -*- coding: utf-8 -*-

value = int(input("A positive num:"))

##%%
#for x in range(0,value):
#    for y in range(0,x + 1):
#        print("*",end =" ")
#    print()

#%%
stars = ""
for x in range(1,value +1):
    stars = stars + "*"
    print(stars)