################################
#Question 65
################################


#Solution 1
# li = [2, 4, 6]
# for i in li:
#     assert i%2 == 0, f"{i} is not an even number"



################################
#Question 66
################################


#Solution 1
# a, exp, b = input().split()
# if exp == '+':
#     print(int(a) + int(b))
# elif exp == '-':
#     print(int(a) - int(b))
# elif exp == '*':
#     print(int(a) * int(b))
# elif exp == '/':
#     print(int(a) / int(b))

#Solution 2
# exp = input()
# print(eval(exp))



################################
#Question 67
################################


#Solution 1
# def bin_search(list, item):
#     bottom, top = 0, len(list) - 1
#     while bottom <= top:
#         middle = (bottom + top) // 2
#         if list[middle] == item:
#             return middle
#         elif list[middle] > item:
#             high = middle - 1
#         else:
#             bottom = middle + 1
#     return None

# lst = [1, 3, 5, 7, 8, 9]
# print(bin_search(lst, 10))



################################
#Question 68
################################


#Solution 1
# import random as rd
# print(rd.uniform(10, 100))



################################
#Question 69
################################


#Solution 1
# import random as rd
# print(rd.uniform(5, 95))

#Solution 2
# import random as rd
# print(rd.random() * 100 - 5)


