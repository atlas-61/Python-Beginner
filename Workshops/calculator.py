# -*- coding: utf-8 -*-
class Mathematic:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2
    
    def add(self):
        return self.n1 + self.n2

    def subs(self):
        return self.n1 - self.n2
    
    def prod(self):
        return self.n1 * self.n2
    
    def div(self):
        if(self.n2 == 0):
            return False
        return self.n1 / self.n2
    
print("Operation?")
print("1: Add")
print("2: Subtraction ")
print("3: Multiplication")
print("4: Division")

op = int(input("-> "))
v1 = int(input("First value: "))
v2 = int(input("Second value: "))
math = Mathematic(v1,v2)

if(op == 1): print("Result: ", str(math.add()))
elif(op == 2): print("Result: ", str(math.subs()))
elif(op == 3): print("Result: ", str(math.prod()))
elif(op == 4): print("Result: ", str(math.div()))
else: print("Invalid operation")
