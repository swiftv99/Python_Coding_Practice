################################
# Question 22
################################


# Solution 1
# line = input().split()
# my_dict = {}
# for x in line:
#     if x not in my_dict.keys():
#         my_dict[x] = line.count(x)
# print(sorted(my_dict.items(), key=lambda a: (a[0], a[1])))

# Solution 2
# line = input().split()
# word = sorted(set(line))
# for x in word:
#     print(f"{x}:{line.count(x)}")

# Solution 3
# line = input().split()
# my_dict = {x:line.count(x) for x in line}
# my_dict = sorted(my_dict.items())
# for x in my_dict:
#     print(f"{x[0]}:{x[1]}") 

# Solution 4
# from pprint import pprint
# line = input().split()
# pprint({x:line.count(x) for x in line})



################################
# Question 23
################################


# Solution 1
# def square(a):
#     return a**2
# num = int(input())
# print(square(num))

# Solution 2
# num = lambda a: a**2
# print(num(int(input())))



################################
# Question 24
################################


# Solution 1
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# def square(num):
#     """Return the square value of the input number.
# The input number must be integer
#     """
#     return num**2
# print(square(2))
# print(square.__doc__)

# Solution 2



################################
# Question 25
################################


# Solution 1
# class Car():
#     brand = 'Audi'
#     def __init__(self, brand=None):
#         self.brand = brand
    
# obj1 = Car('Tesla')
# print(Car.brand, obj1.brand)
# obj2 = Car()
# obj2.brand = 'Mercedes'
# print(Car.brand, obj2.brand)

# Solution 2
