class Person():
    pass
    def a(self):
        print("Hello")
class person():
    pass
    def b(self):
        print("Hello2")
obj = Person()
obj2 = person()
# obj.a()
# obj2.b()
print(obj.__dict__)