# def fib(n):
#     l = [0,1]
#     if n <= 0:
#         print('no should be greater than 0')
#         return
#     elif n == 1:
#         return l[n-1]
#     elif n==2:
#         return l
#     else:
#         for i in range(2,n):
#             l.append(l[i-1] + l[i-2])
#         return l
#
#
# n = int(input('enter no. of elements'))
#
#
# loo=fib(n)
# print( loo)


def fib(n):
    a,b,c = 0,1,0
    while True:
        if c > n: return
        else:
            yield a
            a,b = b,a+b
            c +=1

f= list(fib(2))
for i in f:
    print(i,)
print()
