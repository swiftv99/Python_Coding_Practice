################################
#Question 85
################################


#Solution 1
# lst = [12, 24, 35, 70, 88, 120, 155]
# li = [x for (i, x) in enumerate(lst) if i not in (0, 4, 5)]
# print(li)



################################
#Question 86
################################


#Solution 1
# lst = [12, 24, 35, 24, 88, 120, 155]
# lst.remove(24)
# print(lst)

#Solution 2
# lst = [12, 24, 35, 24, 88, 120, 155]
# li = [i for i in lst if i!= 24]
# print(li)



################################
#Question 87
################################


#Solution 1
# li1 = [1, 3, 6, 78, 35, 55]
# li2 = [12, 24, 35, 24, 88, 120, 155]
# print(set(li1) & set(li2))

#Solution 2
# li1 = [1, 3, 6, 78, 35, 55, 120]
# li2 = [12, 24, 35, 24, 88, 120, 155]
# print(set(li1).intersection(set(li2)))



################################
#Question 88
################################


#Solution 1
# li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# for x in li:
#     if li.count(x) > 1:
#         li.remove(x)
# print(li)

#Solution 2
# def func(li):
#     dict1 = {}
#     for x in li:
#         if x not in dict1:
#             dict1[x] = True
#             yield x
# li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155, 11, 11]
# li2 = list(func(li))
# print(li2) 



################################
#Question 89
################################


#Solution 1
# class Person():
#     def getGender(self):
#         return "Unknown"
# class Male(Person):
#     def getGender(self):
#         return "Male"
# class Female(Person):
#     def getGender(self):
#         return "Female"
# male1 = Male()
# female1 = Female()
# print(male1.getGender())
# print(female1.getGender())



