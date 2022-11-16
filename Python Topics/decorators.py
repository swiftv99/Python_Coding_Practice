# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('************************')
#         func(*args, **kwargs)
#         print('************************')
#     return wrap_func

# @my_decorator
# def hello(greeting, emoji=":("):
#     print(greeting, emoji)

# hello('Hiiiii')
# hello2 = my_decorator(hello)
# hello2()
# my_decorator(hello)()

# from time import time
# def performance(func):
#     def wrap_func(*args, **kwargs):
#         t1 = time()
#         result = func(*args, **kwargs)
#         t2 = time()
#         print(f"It took {t2-t1} s to compute")
#         return result
#     return wrap_func

# @performance
# def long_time():
#     for i in range(100000000):
#         i*5
# long_time()

from decorator_module import *


# @do_twice
# def say_whee():
#     print('Whee!')
# say_whee()


# @do_twice
# def greet(name):
#     print(f"Hello {name}")
# greet('Abdulaziz')


# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi, {name}"
# a = return_greeting('Abdulaziz')
# print(a)


@timer
def waste_some_time(n):
    for _ in range(n):
        sum([i**2 for i in range(10000)])


waste_some_time(1000)
