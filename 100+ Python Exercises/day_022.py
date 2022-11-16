################################
#Question 90
################################


#Solution 1
# txt = input()
# dict1 = {}
# for x in txt:
#     if x not in dict1:
#         dict1[x] = txt.count(x)
# # for k, v in dict1.items():
# #     print(f"{k}, {v}")
# print('\n'.join([f"{k}, {v}" for k, v in dict1.items()]))



################################
#Question 91
################################


#Solution 1
# txt = input()
# print(txt[::-1])

#Solution 2
# txt = input()
# print(''.join(reversed(txt)))



################################
#Question 92
################################


#Solution 1
# def func(txt):
#     for x in range(len(txt)):
#         if x % 2 == 0:
#             yield txt[x]
# txt = input()
# print(''.join(func(txt)))

#Solution 2
# txt = input()
# print(txt[::2])

#Solution 3
# txt = input()
# result = [txt[i] for i in range(len(txt)) if i%2 ==0]
# print(''.join(result))



################################
#Question 93
################################


#Solution 1
# import itertools as itr
# print(list(itr.permutations([1, 2, 3])))



################################
#Question 94
################################


#Solution 1
"""
x + y = 35
4x + 2y = 94
"""
# def func(heads, legs):
#     ans = "No solutions!"
#     for i in range(heads + 1):
#         j = heads - i
#         if 4 * i + 2 * j == legs:
#             return i, j
#     return ans
# heads, legs = 35, 94
# print(func(heads, legs))




