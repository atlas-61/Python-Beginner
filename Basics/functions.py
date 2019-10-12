# -*- coding: utf-8 -*-
def func(name = "Anonymus", sur = ""):
    print("Name: " + name + " " + sur)
    
func("Carl", "Johnson")
func("Ryan")
func()

#%%
def perpTriField(a,b):
    return a*b/2

print(perpTriField(3,4))

#%%
perpTriField2 = lambda a,b: a*b/2

print(perpTriField2(3,4))

x = perpTriField2

print(x(5,5))