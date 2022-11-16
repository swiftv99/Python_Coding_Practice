################################
#Question 100
################################


#Solution 1
# n = int(input())
# dict1 = {}
# li1 = []
# for i in range(n):
#     txt = input()
#     li1.append(txt)
# for i in li1:
#     if i not in dict1:
#         dict1[i] = li1.count(i)
# print(len(dict1.keys()))
# print(*(dict1.values()), sep=' ')



################################
#Question 101
################################


#Solution 1
# txt = input()
# dict1 = {}
# for i in txt:
#     if i not in dict1:
#         dict1[i] = txt.count(i)
# dict1 = sorted(dict1.items(), key=lambda x: (-x[1], x[0]))
# # print(dict1)
# for i in dict1:
#     print(i[0], i[1])

#Solution 2
# txt = input()
# dict1 = {}
# for i in txt:
#     if i not in dict1:
#         dict1[i] = txt.count(i)
# li = list(dict1.items())
# li.sort(key=lambda x: -x[1])
# for i in li:
#     print(i[0], i[1])



################################
#Question 102
################################


#Solution 1
# txt = input()
# digit, letter = 0, 0
# for i in txt:
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         letter += 1
# print(f"Digit - {digit}\nLetter - {letter}")

#Solution 2
# txt = input()
# digit, letter = 0, 0
# for i in txt:
#     digit += i.isdigit()
#     letter += i.isalpha()
# print(f"Digit - {digit}\nLetter - {letter}")



################################
#Question 103
################################


#Solution 1
# def f(n):
#     if n == 0:
#         return 0
#     return f(n-1) + n
# n = int(input())
# print(f(n))

