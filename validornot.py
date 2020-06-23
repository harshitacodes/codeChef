a = int(input("enter the lenght os side"))
b = int(input("enter the lenght os side"))
c = int(input("enter the lenght os side"))
if a+b > c:
	if b + c > a:
		if c + a > b:
			print("valid triangle")
		else:
			print("not valid")	
	else:
		print("not valid")
else:
	print("not valid")			