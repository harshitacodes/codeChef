t = int(input())
c = 0
while c < t:
    g = int(input())
    x = 0
    while x < g:
        i,n,q = map(int, input().split())
        if i==q:
            a = n//2
            print(a)
        else:
            b = n-n//2
            print(b)
        x = x + 1
    c = c + 1