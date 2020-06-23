num = int(input("enter the number"))
if num % 5 == 0:
	if num % 11 == 0:
		print("divisible by both 5 and 11")
	else:
		print("divisible by 5")
else:
	if num % 11 == 0:
		print("divisible by 11")
	else:
		print("none")				