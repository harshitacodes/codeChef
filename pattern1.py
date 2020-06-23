# program to print the pattern of the number
index = 2
a = 3
print(1)
print("\n")
# logic of loop
while index <=5:
	j=index
	while j <= a:
		#  it will print the value of j in a horizontal line
		print(j, end = "")
		j = j + 1
	c = j - 1
	while c > index:
		# decrement of c
		c = c - 1
		# it will print the value of c in the horizontal line
		print(c, end = "")
	print("\n")
	a = a + 2
	index = index + 1	