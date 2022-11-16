################################
#Question 10
################################


#Solution 1
# li = input('Enter a string : ').split(' ')
# li2 = []
# for i in li:
#     if i not in li2:
#         li2.append(i)
# print(' '.join(sorted(li2)))
# print(li2)

#Solution 2
# print(' '.join(sorted(set(input('Enter a string : ').split( )))))



################################
#Question 11
################################


#Solution 1
# lst = input('Enter numbers : ').split(',')
# lst2 = []
# for i in lst:
#     if int(i, 2) % 5 == 0:
#         lst2.append(i)
# print(','.join(lst2))

#Solution 2
# lst = input('Enter numbers : ').split(',')
# lst2 =[i for i in lst if int(i, 2) % 5 == 0]
# print(','.join(lst2))
#Solution 3
# data = input().split(',')
# data = list(filter(lambda i: int(i, 2)%5 == 0, data))
# print(','.join(data))



################################
#Question 12
################################


#Solution 1
        
#Solution 2




################################
#Question 13
################################


#Solution 1


#Solution 2
  