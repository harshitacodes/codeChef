N = int(input("enter the number"))
if N % 2 != 0:
	if N % 3 == 0:
		print("odd and multiple of 3")
	else:
		print("odd")	
else:
	print("not odd")		