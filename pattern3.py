# print the pattern of 1 to 25 numbers	
i = 5
x = 0
# logic of loop
while i <= 25:
	a = i
	if a % 2 == 1:
		x = x + 1
		while x <= a:
			print(x, end = "")
			x = x + 1
	else:
		while a > x:
			print(a, end = "")
			a = a - 1
	x = i		 
	i = i + 5
	print("\n")				

