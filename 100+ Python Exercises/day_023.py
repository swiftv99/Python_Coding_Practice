################################
#Question 95
################################


#Solution 1
# n = int(input())
# li = list(map(int, input().split()))
# li.sort()
# li.reverse()
# print(li)
# for i in li:
#     if i < li[0]:
#         print(i)
#         break

#Solution 2
# n = int(input())
# li = map(int, input().split())
# li = list(set(li))
# li.sort()
# print(li[-2])



################################
#Question 96
################################


#Solution 1
# s = input()
# n = int(input())
# l = len(s)
# for x in range(0, l, 4):
#     if x + 4 >= l:
#         print(s[x:l])
#     else:
#         print(s[x:x+4]) 

#Solution 2
# import textwrap
# s = input()
# n = int(input())
# print(textwrap.fill(s, n))

#Solution 3
# from textwrap import wrap
# s = input()
# n = int(input())
# a = list(wrap(s, n))
# for i in a:
#     print(i)



################################
#Question 97
################################


#Solution 1
# import string
# def func(size):
#     n = size
#     alph = string.ascii_lowercase
#     width = 4 * n - 3
#     ans = []
#     for i in range(n):
#         left = '-'.join(alph[n-i-1:n])
#         mid = left[-1:0:-1] + left
#         final = mid.center(width, '-')
#         ans.append(final)

#     if len(ans) > 1:
#         for i in ans[n-2::-1]:
#             ans.append(i)
#     ans = '\n'.join(ans)
#     print(ans)

# size = int(input())
# func(size)

#Solution 2
# def rangoli(n):
#     # your code goes here
#     l1=list(map(chr,range(97,123)))
#     x=l1[n-1::-1]+l1[1:n]
#     mid=len('-'.join(x))
#     for i in range(1,n):
#         print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-'))
#     for i in range(n,0,-1):
#         print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-')) 
# rangoli(5)



################################
#Question 98
################################


#Solution 1
# import calendar
# mm, dd, yy = map(int, input().split())
# dt = calendar.weekday(yy, mm, dd)
# print(calendar.day_name[dt].upper())



################################
#Question 99
################################


#Solution 1
# m = int(input())
# mlist = set(map(int, input().split()))
# n = int(input())
# nlist = set(map(int, input().split()))
# result = mlist.symmetric_difference(nlist)
# print(*(sorted(result)), sep='\n')

#Solution 2
# m = int(input())
# mlist = set(map(int, input().split()))
# n = int(input())
# nlist = set(map(int, input().split()))
# result = list(mlist ^ nlist)
# for i in result:
#     print(i)


