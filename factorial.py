T = int(input())
for i in range(T):
    factorial = int(input())
    count=0
    j=5
    while(j<=factorial):
        div = factorial//j
        count = count + div
        j = j * 5
    print(count)