T  = int(input())
for i in range(T):
    A,B =map(int,input().split())
    if A>B:
        print(A,A+B)
    else:
        print(B,A+B)