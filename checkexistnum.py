input = int(input("enter the number"))
number = [1,2,3,4,5,6,7]
i = 0
while i < len(number):
    if input == number[i]:
        print("exist")
        break    
    i=i+1
else:    
    print("not exist")