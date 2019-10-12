# -*- coding: utf-8 -*-
students = ["John", "Marie", "Chell"]
print(students)
students.append("Cave")
print(students)
students.remove("John")
print(students)

letters = list(("A","B","C","D","A","A","E","C"))
print(len(letters))
print("Number of A:", letters.count("A"))
print("Number of Chell: ", students.count("Chell"))
print("Index of B: ", letters.index("B"))

students.pop(0)
students.insert(0, "Atlas")
print(students)
students.reverse()
print(students)

st = students #referance type 
st2 = students.copy()

st[0] = "Ricky"
print(students)

students.extend(st2)
print(students)
students.sort()
print(students)

print("Ricky" in st)