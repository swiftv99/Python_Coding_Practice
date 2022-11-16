"""
This is Compile-Time Polymorphism
"""

class Person1():
    def name(self):
        print('My name is Abdulaziz')
    def age(self):
        print("My age is 22")
    def salary(self):
        print("My salary is 1000 $")

class Person2():
    def name(self):
        print("Hi, I'm Mirodil")
    def age(self):
        print("I'm 23 years old")
    def salary(self):
        print("I am currently unemployed")

def func(obj):
    obj.name()
    obj.age()
    obj.salary()

person1 = Person1()
person2 = Person2()
func(person1)
func(person2)