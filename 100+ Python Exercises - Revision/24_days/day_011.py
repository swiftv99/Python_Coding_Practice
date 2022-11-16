################################
#Question 38
################################


#Solution 1
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# print(*(tuple1[:5]), sep=' ')
# print(*(tuple1[5:]), sep=' ')



################################
#Question 39
################################


#Solution 1
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# tuple2 = tuple(i for i in tuple1 if i%2 == 0)
# print(tuple2)

#Solution 2
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# tuple2 = tuple(filter(lambda i: i%2 == 0, tuple1))
# print(tuple2)



################################
#Question 40
################################


#Solution 1
# txt = input()
# if txt == 'Yes' or txt == 'yes' or txt == "YES":
#     print('Yes')
# else:
#     print('No')



################################
#Question 41
################################


#Solution 1
# my_list = [1,2,3,4,5,6,7,8,9,10]
# new_list = list(map(lambda i: i**2, my_list))
# print(new_list)



################################
#Question 42
################################


#Solution 1
# my_list = [1,2,3,4,5,6,7,8,9,10]
# new_list = list(map(lambda i: i**2, filter(lambda i: i%2==0, my_list)))
# print(new_list)



################################
#Question 43
################################


#Solution 1
# my_list = list(filter(lambda i: i%2 == 0, range(1, 21)))
# print(my_list)


