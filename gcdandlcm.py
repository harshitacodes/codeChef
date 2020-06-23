# high time complexicity
# X=int(input())
# for i in range(0,X):
#    x1,y1=map(int,input().split())
#    x=x1
#    y=y1
#    while y1:
#         x1, y1 = y1, x1%y1
#    print(x1,end=" ")
#    print(x*y//x1)


# not optimized... time complexicity is high
N = int(input())
i = 0
lcm = 0
while i < N:
    x, y = map(int, input().split())
    if x > y:
       a = x
    else:
       a = y
    j = 2
    while j < a:
           if (x % j == 0):
               if (y % j == 0):
                   gcd = j
           j = j + 1
    while x:
        if a % x == 0:
            if (a% y == 0):
               lcm = a
               break    
        a = a + 1       
    print("gcd",gcd)
    print("lcm",lcm)   
    i = i + 1