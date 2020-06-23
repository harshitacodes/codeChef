# def decimalToBinary(num):
#     if num > 1:
#         decimalToBinary(num // 2)
#     print(num % 2, end="")


# # decimal number
# number = int(input())

# decimalToBinary(number)

 
T = int(input())
i = 0
while i < T:
	t = int(input())
	j = 0
	result = ""
	while t:
		remainder = t % 2
		div = t//2
		t = div
		result = result + str(remainder)
	a = result[::-1]	
	print(a)	
	i = i + 1