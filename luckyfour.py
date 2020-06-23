T = int(input())
for i in range(T):
    a= input()
    j = 0
    count = 0
    while j < len(a):
        if a[j]== 4:
            count = count + 1
        j = j + 1
    else:
        print(count)




T = int(input())
for i in range(T):
    no_cars = int(input())
    max_speed = input()
    cars_speed = list(max_speed.split())
    first_speed= int(cars_speed[0])
    i=1
    count=1
    for n in range(len(cars_speed)-1):
        x = int(cars_speed[i])
        if x <=first_speed:
            first_car = int(cars_speed[n+1])
            count = count + 1
        else:
            first_speed = int(cars_speed[n])
            cars_speed[i] = first_speed
        i= i + 1
    print(count)