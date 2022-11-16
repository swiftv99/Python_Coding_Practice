################################
#Question 4
################################


#Solution 1
# my_map = map(int, input().split(','))
# my_list = list(my_map)
# my_tuple = tuple(my_list)
# print(my_list, my_tuple, sep='\n')

#Solution 2



################################
#Question 5
################################


#Solution 1
# class Upper():
#     def getString(self):
#         self.text = input()

#     def printString(self):
#         print(self.text.upper())

# obj1 = Upper()
# obj1.getString()
# obj1.printString()

#Solution 2



################################
#Question 6
################################


#Solution 1
# import math
# C, H = 50, 30
# my_list = list(map(int, input().split(',')))
# my_result = []
# for D in my_list:
#     my_result.append(str(round(math.sqrt(2 * C * D / H))))
# print(','.join(my_result))

#Solution 2
# import math
# C, H = 50, 30
# my_list = list(map(int, input().split(',')))
# print(','.join([str(round(math.sqrt(2 * C * D / H))) for D in my_list]))
# print(*(round(math.sqrt(2 * C * D / H)) for D in my_list), sep=',')



################################
#Question 7
################################


#Solution 1
# X, Y = map(int, input().split(','))
# arr1 = []
# for i in range(X):
#     arr2 = []
#     for j in range(Y):
#         arr2.append(i * j)
#     arr1.append(arr2)
# print(arr1)

#Solution 2
# X, Y = map(int, input().split(','))
# print([[i*j for j in range(Y)] for i in range(X)])



################################
#Question 8
################################


#Solution 1
# print(','.join(sorted(input().split(','))))

#Solution 2
# my_list = input().split(',')
# my_list.sort()
# print(','.join(my_list))



################################
#Question 9
################################


#Solution 1
# my_list = []
# while True:
#     txt = input()
#     if len(txt)==0: break
#     my_list.append(txt.upper())  
# print(*(x for x in my_list), sep='\n')

#Solution 2
# def my_func():
#     while True:
#         txt = input()
#         if not txt: return
#         yield txt

# print(*(x.upper() for x in my_func()), sep='\n')