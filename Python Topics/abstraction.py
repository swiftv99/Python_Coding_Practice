from abc import ABC, abstractmethod

class Employee(ABC):
    def emp_id(self, name, id, age, salary):
        pass

class Employee1(Employee):
    def emp_id(self, id):
        print("Employee ID is U1810072")

emp1 = Employee1()
emp1.emp_id(id)