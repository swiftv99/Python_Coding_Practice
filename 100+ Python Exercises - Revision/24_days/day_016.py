################################
#Question 60
################################


#Solution 1
# def f(n):
#     if n == 0:
#         return 0
#     return f(n-1) + 100
# n = int(input('Enter a positive integer: '))
# print(f(n))

#Solution 2
# n = int(input('Enter a positive integer: '))
# f = lambda n: 0 if n == 0 else f(n-1) + 100
# print(f(n))



################################
#Question 61
################################


#Solution 1
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)

# n = int(input('Enter a positive integer: '))
# print(f(n))

#Solution 2
# def f(n):
#     if n < 2:
#         return n
#     return f(n-1) + f(n-2)
# n = int(input('Enter a positive integer: '))
# print(f(n))

#Solution 3
# n = int(input('Enter a positive integer: '))
# f = lambda n: 0 if n == 0 else 1 if n == 1 else f(n-1) + f(n-2)
# print(f(n))

#Solution 4
# n = int(input('Enter a positive integer: '))
# f = lambda n: n if n < 2 else f(n-1) + f(n-2)
# print(f(n))



################################
#Question 62
################################


#Solution 1
# def f(n):
#     if n < 2:
#         return n
#     return f(n-1) + f(n-2)
# n = int(input('Enter a positive integer: '))
# my_list = [str(f(i)) for i in range(n+1)]
# print(','.join(my_list))

#Solution 2
# n = int(input('Enter a positive integer: '))
# f = lambda n: n if n < 2 else f(n-1) + f(n-2)
# my_list = [str(f(i)) for i in range(n+1)]  
# print(','.join(my_list))



################################
#Question 63
################################


#Solution 1
# def f(n):
#     for i in range(n+1):
#         if i%2 == 0:
#             yield i
# n = int(input('Enter a positive integer: '))
# my_list = [str(x) for x in f(n)] 
# print(','.join(my_list))



################################
#Question 64
################################


#Solution 1
# def f(n):
#     for i in range(n+1):
#         if i%5 == 0 and i%7 == 0:
#             yield i
# n = int(input('Enter a positive integer: '))
# values = [str(i) for i in f(n)]
# print(','.join(values))



