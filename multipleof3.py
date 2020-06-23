for j in range:
    sum = 0
    n, d1, d2 = list(map(int, input().split()))
    m = (d1 + d2) % 10
    if n == 2:
        sum = d1 + d2
    elif n == 3:
        sum = d1 + d2 + d
    elif d == 5 or d == 0:
        sum = d1 + d2 + d
    else:
        n = n-3
        sum = (d1+d2)+d+((n//4)*20)
        if n % 4 > 0:
            for i in range(n % 4):
                d = (2*d) % 10
                sum += d
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")