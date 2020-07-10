i = 0
new_list = []
while i < 10:
	user = int(input("enter the number"))
	if user % 2 == 0:
		num = user * 100
		new_list.append(num)
	else:
		num = user * (-1)
		new_list.append(num)
	i = i + 1
print(new_list)	

