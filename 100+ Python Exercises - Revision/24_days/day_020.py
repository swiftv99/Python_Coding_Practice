################################
#Question 80
################################


#Solution 1
# lst = [5, 6, 77, 45, 22, 12, 24]
# print([i for i in lst if i%2 == 1])

#Solution 2
# lst = [5, 6, 77, 45, 22, 12, 24]
# lst2 = list(filter(lambda i: i%2 == 1, lst))
# print(lst2)



################################
#Question 81
################################


#Solution 1
# lst = [12, 24, 35, 70, 88, 120, 155]
# print([i for i in lst if i % 35 != 0])

#Solution 2
# lst = [12, 24, 35, 70, 88, 120, 155]
# result = list(filter(lambda x: x%35 != 0, lst))
# print(result)



################################
#Question 82
################################


#Solution 1
# lst = [12, 24, 35, 70, 88, 120, 155]
# li = [x for (i, x) in enumerate(lst) if i%2 != 0 and i <= 6]
# print(li)

#Solution 2
# lst = [12, 24, 35, 70, 88, 120, 155]
# li = [lst[i] for i in range(len(lst)) if i%2 != 0 and i <= 6]
# print(li)



################################
#Question 83
################################


#Solution 1
# lst = [12, 24, 35, 70, 88, 120, 155]
# li = [x for (i, x) in enumerate(lst) if i < 3 or i > 4]
# print(li)

#Solution 2
# lst = [12, 24, 35, 70, 88, 120, 155]
# li = [lst[i] for i in range(len(lst)) if i < 3 or i > 4]
# print(li)



################################
#Question 84
################################


#Solution 1
# my_list = [[[(k, j, i) for i in range(8)] for j in range(5)] for k in range(3)]
# print(my_list)




