# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return True
#
#         return True
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(2,5)


# num = 1234567
# rev = str(num)[::-1]
# print(int(rev))
#
# def fibonacci (n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#        return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(4))

# a= 'hello'
# b = list(a)
# b[0] = 'H'
# # a = str(b)
#
# print(''.join(b))

# a = [1,2,3,1]
# b = [4,5,6]
# a.sort(reversed(a))
# print(a)

# a = 'pining'
#
# b = 'pining'
# a= list(a)
# b= list(b)
# print(a is b)

# d = {0:0, 1:1}
# def f():
#     d[0] = 4
# f()
# print(d)

# from string import punctuation
#
# def f():
#     for i in a:
#         global l1
#         if i in punctuation or i ==' ':
#             continue
#         else:
#             l1.append(i.capitalize())
#     return l1
#
# a = 'hi ssjdj, as djaid,   assd sjd. '
# l1= []
# l1 = f()
# print(''.join(l1))