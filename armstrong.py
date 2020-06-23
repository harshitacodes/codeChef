# i = 0
# while i < 999:
# 	sum = 0
# 	a = num
# 	while a > 0:
# 	   digit = a % 10
# 	   sum = sum + digit ** 3
# 	   a = a // 10
# 	if num == sum:
# 	   print(num)
# 	i = i +1




# num = int(input("Enter a number: "))
# sum = 0
# a = num
# while a > 0:
#    digit = a % 10
#    sum = sum + digit ** 3
#    a = a // 10
# if num == sum:
#    print(" Armstrong number")
# else:
#    print(" not an Armstrong number")



# i = 1
# sum = 0
# a = i
# while i < 999:
#     while a > 0:
#        digit = a % 10
#        sum = sum + digit ** 3
#        a = a // 10
# 	i = i + 1
# 	if i == sum:
# 		print(i, " Armstrong number")


i = 153
print(1,"Armstrong number")
while i <= 999:
    a = i
    sum=0
    while a > 0:
       digit = a % 10
       sum = sum + digit ** 3
       a = a // 10
    if i == sum:
    	print(sum, " Armstrong number")

    i = i + 1   
	   
