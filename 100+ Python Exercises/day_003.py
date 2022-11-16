################################
#Question 10
################################


#Solution 1
# print(' '.join(sorted(set(input().split(' ')))))

#Solution 2
# my_list = input().split(' ')
# [my_list.remove(x) for x in my_list if my_list.count(x) > 1]
# my_list.sort()
# print(' '.join(my_list))



################################
#Question 11
################################


#Solution 1
# my_list = input().split(',')
# print(*(x for x in my_list if int(x, 2) %5 == 0), sep=',')

#Solution 2
# print(','.join(list(filter(lambda x: int(x,2) %5 == 0, input().split(',')))))

#Solution 3
# print(*(binary for binary in input().split(',') if int(binary,base=2)%5==0),sep=',')



################################
#Question 12
################################


#Solution 1
# print(*(x for x in range(1000, 3001) if x%2 == 0 and (x//10)%2 == 0 and (x//100)%2==0 and (x//1000)%2 == 0), sep=',')
        
#Solution 2
# for x in range(1000, 3001):
#     if x%2 == 0 and (x//10)%2 == 0 and (x//100)%2==0 and (x//1000)%2 == 0:
#         print(x, end=',')



################################
#Question 13
################################


#Solution 1
# import re
# txt = input()
# letters = re.findall("[A-Za-z]", txt)
# digits = re.findall("[0-9]", txt)
# print(f"LETTERS {len(letters)}")
# print(f"DIGITS {len(digits)}")

#Solution 2
# txt = input()
# letters = digits = 0
# for x in txt:
#     if x.isalpha(): letters +=1 
#     elif x.isnumeric(): digits += 1
# print(f"LETTERS {letters}\nDIGITS {digits}")  