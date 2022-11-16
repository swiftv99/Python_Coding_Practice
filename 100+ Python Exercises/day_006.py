################################
#Question 18
################################


#Solution 1
# import re
# my_list = input().split(',')
# values = []
# for x in my_list:
#     if len(x) < 6 or len(x) > 12:
#         continue
#     elif not re.search("[a-z]", x):
#         continue
#     elif not re.search("[0-9]", x):
#         continue
#     elif not re.search("[A-Z]", x):
#         continue
#     elif not re.search("[$#@]", x):
#         continue
#     values.append(x)
# print(','.join(values))

#Solution 2
# import re
# txt = input().split(',')
# my_list = []
# for x in txt:
#     a = 0
#     a += 6 <= len(x) <= 12
#     a += bool(re.search("[A-Z]", x))
#     a += bool(re.search("[a-z]", x))
#     a += bool(re.search("[0-9]", x))
#     a += bool(re.search("[@#$]", x))
#     if a == 5:
#         my_list.append(x)
# print(','.join(my_list))



################################
#Question 19
################################


#Solution 1
# my_list = []
# while True:
#     line = input()
#     if not line: break
#     my_list.append(tuple(line.split(',')))
# print(sorted(my_list, key=lambda i: (i[0], int(i[1]), int(i[2]))))

#Solution 2


