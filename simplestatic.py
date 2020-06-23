t=int(input())
for i in range(t):
    n,k = map(int,input().split())
    b = list(map(int,input().split()))
    b.sort()
    print(b)
    sum=0
    for j in range(k,n-k):
        sum=sum+b[j]
        print(sum)
    c = (n - 2*k)
    average=(sum/c)
    print(average)