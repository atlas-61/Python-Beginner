# -*- coding: utf-8 -*-
tupleList = (6,5,3,"Vincent",(2,3,6),[]) #parenthesis are different, read-only
normList = [6,5,3, "Vincent",[2,3,6], ()]

print("Tuple: ",tupleList)
print("List: ",normList)

normList[3] = "Jules"
#tupleList[3] = "Jules" not possible

print("Tuple: ",tupleList)
print("List: ",normList)

print("Tuple: ", tupleList[-2])
print("List: ", normList[-2])

print("Tuple: ", tupleList[2:3]) #if tuple has one item or you show one item, you ll see (3,) in output
print("List: ", normList[2:3])