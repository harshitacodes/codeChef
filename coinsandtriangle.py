t = int(input())
for i in range(t):
    n = int(input())
    a = 0
    b = 0
    c = 1
    while b <= n:
        b = b + c
        c = c + 1
    r = c - 2
    print(r)

# n=int(input())
# for i in range(n):
#     x=int(input())
#     c=0
#     while (c<x):
#         c=c+1
#         x=x-c
#     print(c)