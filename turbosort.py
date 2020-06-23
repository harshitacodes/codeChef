# n=int(input())
# m=[]
# for i in range(n):
#     m.append(int(input()))
# z=sorted(m)
# for i in z:
#     print(i)


# t = int(input())

# list = []
# for i in range(t):
#     list.append(int(input()))
    
# list = (sorted(list))

# for i in range(len(list)):
#     print(list[i])

# a = int(input())
# total = []
# for i in range(a):
#     b = int(input())
#     total.append(b)
# total.sort()
# for j in total:
#     print(j)




N = int(input())
j = 0
number = []
while j < N:
	n = int(input())
	number.append(n)
	j = j + 1
n=0
while n<len(number):
    i=0
    while i<len(number)-1:
        if number[i] > number[i+1]:
            number[i],number[i+1]=number[i+1],number[i]
        else:
            number[i],number[i+1]=number[i],number[i+1]
        i=i+1
    n=n+1
t = 0
while t < len(number):
	print(number[t])
	t = t + 1 