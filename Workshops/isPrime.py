# -*- coding: utf-8 -*-

value = int(input("Positive num:"))
flag = True
if value == 1:
    print("Not prime!")
    flag = False
elif value == 2:
   flag = True
elif value % 2 == 0:
    print("Not prime!")
    flag = False
else:
  for divider in range(2,value):
      if value % divider == 0:
          print("Not prime!")
          flag = False
          break
      
if flag:
    print("Prime found!")
            