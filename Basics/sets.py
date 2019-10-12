# -*- coding: utf-8 -*-
studentSet = {"Atlas","Jack","Ryan","Booker","Liz",
              "Zachary","Marvin","Butch","Jesse"}


#print(studentSet)

for student in studentSet:
    print(student)
    
print()
print("Liz" in studentSet)

studentSet.add("Walter")
print(studentSet)

studentSet.update(["Yınkırt","Mızkırt","Çıkırt"])
print(studentSet)

ss = studentSet
ss.remove("Yınkırt")
print(ss)

ss.discard("Yınkırt") #if yınkırt already deleted or not found in set,discard not return error
print(ss)

x = ss.pop() #pop deletes first item in sets but first item can change every update or pushing
print(x)
print(ss)

del studentSet #deletes data and variable itself