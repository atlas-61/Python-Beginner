# -*- coding: utf-8 -*-
#%% basics
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
    
    
math = Mathematic(3,2)
print(str(math.div()))

#%% property
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person = Person("Jonas", "Rich", "22")
print(person.firstName)

class Worker(Person):
    def __init__(self, salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self, creditCardNum):
        self.ccNum = creditCardNum
        
Noah = Worker(1200)
Hannah = Customer(457966587)
Noah.firstName = "Noah"

        
        
        
        
        