N = int(input())
i = 1
while i < N:
    (a, b, c) = map(int, input().split())
    if a>b:
        if a>c:
            if b>c:
                print(b)
            else:
                print(c)
        else:
            print(a)
    elif b>c:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        if b>a:
            print(b)
        else:
            print(a)
    i = i + 1