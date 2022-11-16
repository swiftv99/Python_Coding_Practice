################################
#Question 14
################################


#Solution 1
# import re
# txt = input()
# upper = re.findall("[A-Z]", txt)
# lower = re.findall("[a-z]", txt)
# print(f"UPPER CASE {len(upper)}\nLOWER CASE {len(lower)}") 

#Solution 2
# txt = input()
# upper = lower = 0
# for x in txt:
#     upper += x.isupper()
#     lower += x.islower()
# print("UPPER CASE {}\nLOWER CASE {}".format(upper, lower))

#Solution 3
# txt = input()
# upper = sum(1 for i in txt if i.isupper())
# lower = sum(1 for i in txt if i.islower())
# print("UPPER CASE {}\nLOWER CASE {}".format(upper, lower))



################################
#Question 15
################################


#Solution 1
# a = int(input())
# sum = 0
# for x in range(1, 5):
#     for y in range(x):
#         sum += 10**y * a
# print(sum)

#Solution 2
# a = input()
# print(sum(int(a*i) for i in range(1,5)))