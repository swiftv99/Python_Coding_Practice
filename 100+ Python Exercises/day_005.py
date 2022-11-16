################################
#Question 16
################################


#Solution 1
# my_list = list(map(int, input().split(',')))
# print(*([x**2 for x in my_list if x%2 != 0]), sep=',')

#Solution 2
# my_list = [str(int(x)**2) for x in input().split(',') if int(x)%2]
# print(','.join(my_list))



################################
#Question 17
################################


#Solution 1
# sum = 0
# while True:
#     txt = input()
#     if not txt:
#         break
#     else:
#         a, price = txt.split(' ')
#         if a == 'D':
#             sum += int(price)
#         elif a == "W":
#             sum -= int(price)
# print(sum)

#Solution 2
