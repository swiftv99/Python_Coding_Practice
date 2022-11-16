################################
#Question 70
################################


#Solution 1
# import random as rd 
# print(rd.choice([i for i in range(11) if i%2 == 0]))



################################
#Question 71
################################


#Solution 1
# import random as rd
# print(rd.choice([i for i in range(10, 151) if i%35 == 0]))



################################
#Question 72
################################


#Solution 1
# import random as rd
# print(rd.choices(range(100, 201), k=5)) # with duplicates

#Solution 2
# import random as rd
# print(rd.sample(range(100, 201), k=5)) # without duplicates


################################
#Question 73
################################


#Solution 1
# import random as rd
# print(rd.sample([i for i in range(100, 201) if i%2 == 0], k=5))

#Solution 2
# import random as rd
# print(rd.sample(range(100, 201, 2), k=5))


################################
#Question 74
################################


#Solution 1
# import random as rd
# lst = [i for i in range(1, 1001) if i%35 == 0]
# print(rd.sample(lst, k=5))



