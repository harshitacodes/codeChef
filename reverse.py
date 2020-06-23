# program will print the reverse of any number
# more optimized , to  print the reverse of the number
n = int(input("enter the number"))
x = 0
if n < 0:
	n = (-n) 
while n > 0:
	x = (x*10) +(n % 10)
	n = n // 10
print(x)