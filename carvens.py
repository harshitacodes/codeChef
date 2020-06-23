# T = int(input())
# for i in range(T):
#     nCar = int(input())
#     for j in (nCar):

#         count = 1
#         max = 0
#         for i in range(0,len(nMax)-1):
#             if nMax[i] > nMax[i+1]:
#                 max = nMax[i]
#                 count+=1
#         print(count)



T = int(input())
for i in range(T):
    n_cars = int(input())
    max_cars = list(map(int,input().split()))
    a= int(max_cars[0])
    j=1
    count=1
    for x in range(len(max_cars)-1):
        b = max_cars[j]
        if b <= a:
            a = max_cars[x+1]
            count=count + 1
        else:
            a = max_cars[x]
            max_cars[j] = a
        j= j + 1
    print(count)
