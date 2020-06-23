input=int(input("enter the num"))
a=1
sum=0
while a <=input:
    if input%a==0:
        sum=sum+a
        if sum == input:
            print(input, "is a perfect number")
            break
    a=a+1        
else:
    print("not a perfect number")
    