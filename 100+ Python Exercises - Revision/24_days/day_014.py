################################
#Question 51
################################


#Solution 1
# def division(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         return 'You divided by zero'
#     except Exception as err:
#         return "Any other exception"
#     finally:
#         return 'Final message'
# print(division(5, '0'))

#Solution 2
# try:
#     a = lambda a, b: a/b
# except ZeroDivisionError as err:
#     print("You divided by zero")
# except Exception as err:
#     print("Any other exception")
# finally:
#     print("Final message")
# print(a(5, 1))



################################
#Question 52
################################


#Solution 1
# class CustomException(Exception):
#     def __init__(self, string):
#         self.string = string

# num = int(input())
# try:
#     if num < 10:
#         raise CustomException("Input is less than 10")
#     elif num > 10:
#         raise CustomException("Input is greater than 10")
# except CustomException as ce:
#     print("The error raised:" + ce.string)



################################
#Question 53
################################


#Solution 1
# print(input("Enter your email address: ").split('@')[0])

#Solution 2
# import re
# email = "john@google.com elise@python.com"
# pattern = "(\w+)@\w+.com"
# answer = re.findall(pattern, email)
# print(answer)


