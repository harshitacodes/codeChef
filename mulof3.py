# t=int(input())
# for i in range(t) :
# 	k,d0,d1=map(int,input().split())
# 	sum =d0 + d1
# 	for i in range(k):
# 		if sum!=10 and k>2:
# 			mod=sum % 10
# 			sum= sum + mod
# 			if sum!=10 and sum!=20 :
# 			sum=sum + 20*((k-3)//4)
# 			x=(k-3)%4
# 			for j in range(x) :
# 				temp2=sum%10
# 				sum=sum+temp2
# 		print(sum)
# 	if sum%3 ==0:
# 		print('YES')
# 	else :
# 		print('NO')

t=int(input())
for i in range(t) :
	k,d0,d1=map(int,input().split(' '))
	s=d0+d1
	if s!=10 and k>2 :
		temp=s%10
		s=s+temp
		if s!=10 and s!=20 :
			s=s + 20*((k-3)//4)
			# print(s)
			x=(k-3)%4
			for j in range(x) :
				temp2=s%10
				s+=temp2
				# print(s)
	    	
	if s%3 ==0 :
		print(s,'YES')
	else :
		print('NO')



	# digit = 0
	# sum = 0
	# while a > 0:
	# 	digit = a % 10
	# 	sum =  sum + digit
	# 	a =  a // 10
	# # it will print the sum of digits
	# print(sum)
	# i = i + 1