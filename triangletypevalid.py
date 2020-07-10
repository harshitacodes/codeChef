a = int(input("enter the lenght os side"))
b = int(input("enter the lenght os side"))
c = int(input("enter the lenght os side"))
if a + b > c and b + c > a and c + a > b:
	if a == b and b == c and a == c:
		print("equilateral ")
	elif a == c or b == c or a == b:
		print("isoceles")
	else:	
		print("scalar")				
else:
	print("not valid")			

