################################
#Question 47
################################


#Solution 1
# import math
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2

# obj = Circle(5)
# print(obj.area())



################################
#Question 48
################################


#Solution 1
# class Rectangle():
#     def __init__(self, length, width):
#         self.l = length
#         self.w = width

#     def area(self):
#         return self.l * self.w

# rect1 = Rectangle(5, 4)
# print(rect1.area())



################################
#Question 49
################################


#Solution 1
# class Shape():
#     def __init__(self):
#         pass

#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, length=0):
#         Shape.__init__(self)
#         self.len = length

#     def area(self):
#         return self.len**2

# sqr1 = Square(5)
# print(sqr1.area())
# print(Square().area())



################################
#Question 50
################################


#Solution 1
# raise RuntimeError("Something went wrong")


