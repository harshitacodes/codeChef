# Write a program to create a list of 7 numbers from the user, print true if the complete list consists of consecutive numbers or not.
i = 0
list1 = []
while i < 7:
	n = int(input("enter the number"))
	list1.append(n)
	i=i+1
j = 1
index1 = list1[0] + 1
while j < len(list1):
	if index1 == list1[j]:
		index1=index1+1
		j = j +1 
	else:
		print("not consecutive")
		break
else:
	print("consecutive") 