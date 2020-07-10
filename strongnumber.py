# program to check whether given number is strong number or not
Number = int(input(" Please Enter any Number: "))
Sum = 0
a = Number
# logic
while(a > 0):
    Factorial = 1
    i = 1
    Rem = a % 10
    while(i <= Rem):
        Factorial = Factorial * i
        # finding the factorial of one by one all digit
        i = i + 1
    Sum = Sum + Factorial
    a = a // 10
# print if number is strong or not 
if (Sum == Number):
    print(Number , "is a Strong Number")
else:
    print(Number ,"is not a Strong Number")