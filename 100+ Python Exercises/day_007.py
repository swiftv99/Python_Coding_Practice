################################
#Question 20
################################


#Solution 1
# class DivisibleBy7():
#     def iterate(self, num):
#         return [x for x in range(num + 1) if x % 7 == 0]
# obj1 = DivisibleBy7()
# print(*(obj1.iterate(int(input()))), sep='\n')

#Solution 2
# class DivisibleBy7():
#     def iterate(self, num):
#         for x in range(num + 1):
#             if x % 7 == 0: yield x
# obj1 = DivisibleBy7()
# for x in obj1.iterate(int(input())):
#     print(x)



################################
#Question 21
################################


#Solution 1
# from math import sqrt
# x, y = 0, 0
# while True:
#     line = input()
#     if not line: break
#     line = line.split()
#     if line[0] == 'UP':
#         y -= int((line[1]))
#     elif line[0] == 'DOWN':
#         y += int(line[1])
#     elif line[0] == 'LEFT':
#         x -= int(line[1])
#     elif line[0] == 'RIGHT':
#         x += int(line[1])
# print(round(sqrt(x**2 + y**2)))

#Solution 2



