# program to check the number is prime or not
a = int(input("enter the number to know is it prime or not "))
i = 2
# logic
if a == 1:
	print("not prime or not composite")
else:	
	while i * i <= a:
		if (a%i==0):
			print('not prime number')
			break
		i=i+1
	else:
		print("yes prime")

