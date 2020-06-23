# Write a program to create a list of 10 numbers from the user, print true if the list is a progression. A progression is a list in which each two consecutive(nearby) elements have a constant difference.
i = 0
list1 = []
# loop for the 10 times user input
while i < 4:
	n = int(input("enter the number"))
	list1.append(n)
	i=i+1
index1 = list1[1] - list1[0]
j = 0
while j < len(list1) - 1:
	# check the difference is equal or not
	if index1 == list1[j + 1] - list1[j]:
		j = j + 1
	else:
		print("False")
		break
else:
	print("true") 