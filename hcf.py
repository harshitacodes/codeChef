a = int(input("enter any number"))
b = int(input("enter any number"))
if a > b:
    x = b
else:
    x = a
i=1
while i < x:
    if (a % i == 0):
        if (b % i == 0):
            hcf=i
    i = i + 1        
print("hcf of both is",hcf)
    

# N = int(input())
# j = 0
# while j < N:
# 	a, b = map(int, input().split())	
# 	if a > b:

# 	a, b = map(int, input().split())	
# 	if a > b:
# 	    x = a
# 	else:

# 	print(lcm)   	
# 	i = i + 1

# N = int(input())
# i = 0
# lcm = 0
# coooo=0
# while i < N:
#     x, y = map(int, input().split())
#     if x > y:
#        a = x
#     else:
#        a = y
#     j = 1
#     while j < a/2:
#            if (x % j == 0):
#                if (y % j == 0):
#                    gcd = j
#            j = j + 1
#            print(j, "kjskj")
#     while (True):
#         if a % x == 0:
#             if (a% y == 0):
#             	print(a)
#             	lcm = a
#             	break   
# X=int(input())
# for i in range(0,X):
#    x1,y1=map(int,input().split())
#    x=x1
#    y=y1
#    while y1:
#         x1, y1 = y1, x1%y1
#    print(x1,end=" ")
#    print(x*y//x1)



