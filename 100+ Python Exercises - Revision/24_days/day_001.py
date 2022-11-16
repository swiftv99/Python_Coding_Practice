################################
#Question 1
################################


#Solution 1
# for i in range(2000, 3201):
#     if i%7 == 0 and i%5 != 0:
#         print(i, end=', ')
# print('\b')

#Solution 2
# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=',')



################################
#Question 2
################################


#Solution 1
# n = int(input("Enter a number : "))
# fac = 1
# for i in range(1, n+1):
#     fac *= i
#     print(fac, end=',')
# print('\b')

#Solution 2
# n = int(input("Enter a number : "))
# i = 1
# fac = 1
# while i <= n:
#     fac *= i
#     i += 1
#     print(fac, end=',')
# print('\b')



################################
#Question 3
################################


#Solution 1
# n = int(input("Enter a number : "))
# my_dict = {}
# for i in range(1, n+1):
#     my_dict[i] = i**2
# print(my_dict)

#Solution 2
# n = int(input("Enter a number : "))
# print({i:i**2 for i in range(1, n+1)})