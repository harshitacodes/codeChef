# program to print the N number of prime number given by user
n = int(input("enter the number")) 
counter = 0
num = 2
while counter < n:
	i = 2
	# logic
	while i * i <= num:
		if num % i == 0:
			break
		i = i + 1
	else:
		# print prime number
		print(num)
		counter = counter + 1
	num = num + 1			
