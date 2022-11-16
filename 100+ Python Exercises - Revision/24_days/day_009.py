################################
#Question 26
################################


#Solution 1
# def sum(num1, num2):
#     return num1+num2
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# print(sum(a, b))

#Solution 2
# sum = lambda n1, n2: n1 + n2
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# print(sum(a, b))



################################
#Question 27
################################


#Solution 1
# type_casting = lambda num: str(num)
# num = input("Enter an integer: ")
# print(type_casting(num))



################################
#Question 28
################################


#Solution 1
# sum = lambda a, b: int(a) + int(b)
# a, b = input().split()
# print(sum(a, b))



################################
#Question 29
################################


#Solution 1
# concat = lambda t1, t2: t1+t2
# txt1, txt2 = input().split()
# print(concat(txt1, txt2))



################################
#Question 30
################################


#Solution 1
# def maximum(s1, s2):
#     if len(s1) > len(s2):
#         return s1
#     elif len(s1) < len(s2):
#         return s2
#     else:
#         return f"{s1}\n{s2}"
# s1, s2 = input().split()
# print(maximum(s1, s2))

#Solution 2
# func = lambda s1, s2: print(max((s1, s2), key=len)) if len(s1)!= len(s2) else print(f"{s1}\n{s2}")
# func(*(input().split()))


