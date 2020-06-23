a = int(input("enter the length of side"))
b = int(input("enter the length of side"))
c = int(input("enter the length of side"))
if a == b and  b == c and c == a:
	print("equilateral")
elif a == c or  b == c or a == b:
	print("isosceles")
else:	
	print("scalar")	