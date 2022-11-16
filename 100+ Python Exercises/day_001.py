################################
#Question 1
################################


#Solution 1
# for x in range(2000, 3201):
#     if x % 7 == 0 and x % 5 != 0:
#         print(x, end=', ')
# print('\n')

#Solution 2
# print(*(x for x in range(2000, 3201) if x%7 == 0 and x%5 != 0), sep=', ')



################################
#Question 2
################################


#Solution 1
# a, fact = int(input('Enter an integer number: ')), 1
# for x in range(1, a+1): fact *= x
# print(fact)

#Solution 2
# a = int(input('Enter an integer number: '))
# def factorial(a): return 1 if a < 1 else a*factorial(a-1)
# print(factorial(a))



################################
#Question 3
################################


#Solution 1
# n = int(input('Enter an integer number: '))
# my_dict = {}
# for x in range(1,n+1): my_dict[x] = x**2
# print(my_dict)

#Solution 2
# n = int(input('Enter an integer number: '))
## my_dict = {x: x**2 for x in range(1,n+1)}
# print({x: x**2 for x in range(1,n+1)})
## print(dict(enumerate([i*i for i in range(1, n+1)], 1)))