# -*- coding: utf-8 -*-

#r Read, a Append, w Write, x Create
f = open("customers.txt")

print(f.read()) #read(10) reads first 10 character
print("* * * * * * * * * *")
print(f.readline()) #after f.read() there is no more lines so it returns blank

for line in f:
    print(line)

fileToAppend = open("students.txt", "a")

fileToAppend.write("\n")
fileToAppend.write("Lando Norris")
fileToAppend.close()    
f.close()

import os
if os.path.exists("file name"): #checks file exists
    os.remove("file name") #removes the file
else:
    print("No such a file or directory!")
    
os.rmdir("directory name") #removes directory