T = int(input())
for i in range(T):
    h,c,t = map(float,input().split())
    grade = 5
    if (h > 50 and c < 0.7 and t> 5600):
        grade = 10
    elif(h > 50 and c < 0.7):
        grade = 9
    elif(c < 0.7 and t > 5600):
        grade = 8
    elif(h > 50 and t> 5600):
        grade = 7
    elif(h > 50 or c < 0.7 or t > 5600):
        grade = 6
    print(grade)