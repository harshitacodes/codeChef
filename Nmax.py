N = int(input("enter the number"))
i = 0
maximum = 0
while i < N:
	number = int(input("enter the number"))
	if number >maximum:
		maximum = number
	i = i + 1
print(maximum)		