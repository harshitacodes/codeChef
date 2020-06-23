
N = int(input("enter the number"))
res = 1
p = 2
while p <= N:
	c = 0 
	while N % p == 0:
		c = c +  1
		N = N // p
	
	res = res * (c + 1)
	print(res)
	p = p + 1	
print(res)	