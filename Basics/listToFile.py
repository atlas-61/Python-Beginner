# -*- coding: utf-8 -*-
students = ["Marie", "Walt.Jr", "Atlas", "Carmen"]

file = open("students2.txt", "a")

for names in students:
    file.write(names)
    file.write("\n")
    
file.close()