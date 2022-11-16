################################
#Question 4
################################


#Solution 1
# li = map(int, input('Enter a number : ').split(','))
# my_li = list(li)
# print(my_li)
# print(tuple(my_li))

#Solution 2
# my_li = input('Enter a number : ').split(',')
# print(my_li)
# print(tuple(my_li))



################################
#Question 5
################################


#Solution 1
# class MyClass:
#     def __init__(self):
#         self.txt = ''
    
#     def getString(self):
#         self.txt = input("Enter a string : ")

#     def printString(self):
#         print(self.txt.upper())

# obj1 = MyClass()
# obj1.getString()
# obj1.printString()

#Solution 2
# class MyClass:
#     def getString(self):
#         self.txt = input("Enter a string : ")

#     def printString(self):
#         print(self.txt.upper())

# obj1 = MyClass()
# obj1.getString()
# obj1.printString()



################################
#Question 6
################################


#Solution 1
# import math
# D = map(int, input("Enter a list of integers :\n").split(','))
# Q = []
# for i in D:
#     Q.append(round(math.sqrt(10 * i / 3)))
# print(*Q, sep=',')

#Solution 2
# import math
# D = map(int, input("Enter a list of integers :\n").split(','))
# Q = []
# for i in D:
#     Q.append(str(round(math.sqrt(10 * i / 3))))
# print(','.join(Q))



################################
#Question 7
################################


#Solution 1
# x = int(input('Enter the value of X : '))
# y = int(input('Enter the value of Y : '))
# li = []
# for i in range(x):
#     temp = []
#     for j in range(y):
#         temp.append(i*j)
#     li.append(temp)
# print(li) 


#Solution 2
# x, y = map(int, input('Enter two values : ').split(','))
# print([[i*j for j in range(y)] for i in range(x)])



################################
#Question 8
################################


#Solution 1
# li = input("Values : ").split(',')
# li.sort()
# print(','.join(li))

#Solution 2



################################
#Question 9
################################


#Solution 1
# li = []
# while True:
#     txt = input('Enter string : ')
#     if len(txt) == 0 : break 
#     li.append(txt.upper())
# print(*li, sep='\n')  

#Solution 2
# def my_iter():
#     while True:
#         txt = input("Enter string : ")
#         if len(txt) == 0: 
#             return
#         yield txt.upper()
# print(*(i for i in my_iter()), sep='\n')