class Employee():
    def __init__(self):
        self.name = "Abdulaziz"
        self._age = 22
        self.__id = 'U1810072'
    def earn(self):
        print(f"ID is: {self.__id}")
    def set_earn(self, id):
        self.__id = id

# obj = Employee()
# print(obj.name)
# print(obj._age)
# print(obj.__id)

obj = Employee()
obj.earn()

obj.__id = 'U1810031'
obj.earn()

obj.set_earn("U1810038")
obj.earn()