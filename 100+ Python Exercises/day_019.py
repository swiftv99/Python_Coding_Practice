################################
#Question 75
################################


#Solution 1
# import random as rd
# print(rd.randint(7, 15))

#Solution 2
# import random as rd
# print(rd.randrange(7, 16))



################################
#Question 76
################################


#Solution 1
# import zlib
# txt = "hello world!hello world!hello world!hello world!"
# s = bytes(txt, 'utf-8')
# a = zlib.compress(s)
# print(a)
# print(zlib.decompress(a))



################################
#Question 77
################################


#Solution 1
# from timeit import Timer
# t = Timer("for i in range(100): 1 + 1")
# print(t.timeit())

#Solution 2
# from datetime import datetime
# t1 = datetime.now()
# print(t1)
# for i in range(100): 
#     x = 1 + 1
# t2 = datetime.now()
# print(t2)
# exc_time = t2 - t1
# print(exc_time)



################################
#Question 78
################################


#Solution 1
# import random as rd
# lst = [3, 6, 7, 8]
# rd.shuffle(lst)
# print(lst)



################################
#Question 79
################################


#Solution 1
# subject = ['I', 'You']
# verb = ['Play', 'Love']
# objects = ['Hockey', 'Football']
# for i in subject:
#     for j in verb:
#         for k in objects:
#             print(f"{i} {j} {k}")


