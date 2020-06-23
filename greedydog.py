n=int(input())
for i in range(0,n):
    l=[]
    x,y=map(int,input().split())
    for j in range(1,y+1):
        f=x%j
        l.append(f)
    print(l)
    print(l[-1])

