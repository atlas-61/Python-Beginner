# -*- coding: utf-8 -*-
#substring
msg = "Hello World!"
print(msg[0:5]) # not include fifth charecter
nw_msg = msg[6:]
print(nw_msg)
nw_msg = msg[:6]
print(nw_msg)

#len
print(msg[len(msg) - 1])

# lower upper
print(msg.upper())
print(msg.lower())

#replace
print(msg.replace("!","?"))
print(msg.replace("l","M"))

#split n strip
info = "John Doe 27 Place"
print(info.split()) #default func splits by space and uses strip()
info = "    John;Doe;27;Place  "
print(info.split(";"))

info = "    John;Doe;27;Place  ".strip()
print(info.split(";"))
print(info.split(";")[3])

#input
name = input("Name: ")
v1 = input("Value1: ")
v2 = input("Value2: ")
print(v1 + v2)
print(int(v1 + v2) + 3)
print(int(v1) + int(v2))