################################
#Question 54
################################


#Solution 1
# print(input('Enter your email: ').split('@')[1].split('.')[0])

#Solution 2
# import re
# email = input("Enter your email: ")
# pattern = "\w+@(\w+).com"
# answer = re.findall(pattern, email)
# print(answer)


################################
#Question 55
################################


#Solution 1
# txt = input().split()
# my_list = []
# for x in txt:
#     if x.isdigit():
#         my_list.append(x)
# print(my_list)

#Solution 2
# import re
# txt = input()
# print(re.findall("\d+", txt))


################################
#Question 56
################################


#Solution 1
# print(u"hello world")



################################
#Question 57
################################


#Solution 1
# s = input()
# u = s.encode('utf-8')
# print(u)



################################
#Question 58
################################


#Solution 1
# -*- coding: utf-8 -*-



################################
#Question 59
################################


#Solution 1
# n = int(input("Enter a positive integer: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i / (i + 1)
# print(round(sum, 2))



