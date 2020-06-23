T=int(input()) 
while T > 0:
    N=int(input())    
    a=list(map(int,input().split())) 
    b=[] 
    for i in a:
        if(i not in b):
            b.append(i)
    x=N-len(b) 
    print(x)


# T = int(input())
# i = 0
# while i < T:
#     N = int(input())
#     a = list(map(int,input().split())) 
#     # print(a)
#     b = []
#     j = 0
#     while j < len(a):
#         p = a[j]
#         if p not in b:
#             b.append(p)
#         j = j + 1
#     m = N - len(b)
#     print(m)
#     i = i + 1


