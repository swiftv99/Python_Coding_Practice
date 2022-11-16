"""
This is Run-Time Polymorphism
"""
class Employee():
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
    def earn(self):
        pass

class Employee1(Employee):
    def earn(self):
        print('No money')

class Employee2(Employee):
    def earn(self):
        print("Some money")

a = Employee1('Abdulaziz', 22, 'U1810072', 1000)
a.earn()
b = Employee2('Mirodil', 22, 'U1810031', 300)
b.earn()