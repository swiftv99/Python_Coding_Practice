################################
#Question 31
################################


#Solution 1
# func = lambda: {i:i**2 for i in range(1, 21)}
# print(func())



################################
#Question 32
################################


#Solution 1
# def square():
#     my_dict = {i:i**2 for i in range(1, 21)}
#     return my_dict.keys()
# print(square())



################################
#Question 33
################################


#Solution 1
# my_list = lambda: [i**2 for i in range(1,21)]
# print(my_list())



################################
#Question 34
################################


#Solution 1
# my_list = lambda: print([i**2 for i in range(1, 21)][0:5])
# my_list()



################################
#Question 35
################################


#Solution 1
# my_list = lambda: print([i**2 for i in range(1, 21)][-5:])
# my_list()

#Solution 2
# def last_5():
#     my_list = [i**2 for i in range(1, 21)]
#     return my_list[-5:]
# print(last_5())


################################
#Question 36
################################


#Solution 1
# my_list = lambda n: print(*([i**2 for i in range(1, n+1)][5:]), sep='\n')
# my_list(20) 



################################
#Question 37
################################


#Solution 1
# my_tuple = lambda n: print(*tuple(i**2 for i in range(1, n+1)), sep='\n')
# my_tuple(20)
# print(type(my_tuple))



