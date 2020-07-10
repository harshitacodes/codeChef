a = int(input("enter the lenght os side"))
b = int(input("enter the lenght os side"))
c = int(input("enter the lenght os side"))
if a == b:
	if b == c:
		print("equilateral")
	else:
		print("isoceles")
elif a == c:
	print("isoceles")
elif b == c:
	print("isoceles")
else:	
	print("scalar")				