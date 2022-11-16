"""
map(function, iterables)
filter(function, iterable)
"""
# a = 1
# b = 1
# print(a == b)
# print(a is b)

class A:
    def foo(self):
        print("A")


class B(A):
    def foo(self):
        print("B")
        super().foo()


class C(A):
    def foo(self):
        print("C")
        super().foo()


class D(B, C):
    # def foo(self):
    #     print("D")
    #     super().foo()
    pass

D().foo()