num = int(input("enter the number"))
a = ['a','1','2','5','b','q']
length = len(a)
b = length - num
while b < length:
	print(a[b])
	b = b + 1