# program to check given number is pallindrome or not
num=int(input("Enter a number:"))
a=num
reverse=0
# logic 
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if(a==reverse):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")