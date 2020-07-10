n = int(input("enter the number"))
i = 0
sum = 0
odd = 1
while i < n:
	sum = sum + odd
	odd = odd + 2
	i = i + 1
print(sum)	