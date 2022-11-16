# def my_func9():
#     pass
#     # def special_for(iterable):
#     #     iterator = iter(iterable)
#     #     while True:
#     #         try:
#     #             print(iterator)
#     #             print(next(iterator))
#     #         except StopIteration:
#     #             break

#     # special_for([1,2,3])

#     class MyGen():
#         current = 0
#         def __init__(self, first, last):
#             self.first = first
#             self.last = last 

#         def __iter__(self):
#             return self

#         def __next__(self):
#             if MyGen.current < self.last:
#                 num = MyGen.current
#                 MyGen.current += 1
#                 return num
#             raise StopIteration

#     gen = MyGen(0,100)
#     for x in gen:
#         print(x)

#     def fib(number):
#         a, b = 0, 1
#         for _ in range(number+1):
#             yield a
#             a, b = b, a + b
        
#     i = 0
#     for x in fib(25):
#         print(f'fib{i} =', x)
#         i += 1

# # def my_iter(iterable):
# #     my_iterator = iter(iterable)
# #     while True:
# #         try: 
# #             print(next(my_iterator))
# #         except StopIteration:
# #             break

# # my_iter([1, 2, 3, 4])

# class MyIter():
#     current = 0
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyIter.current < self.last:
#             n = MyIter.current
#             MyIter.current += 1
#             return n
#         raise StopIteration

# obj1 = MyIter(0, 20) 
# for i in obj1:
#     print(i)