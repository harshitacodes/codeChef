# insertion sort
N = int(input())
k = 0
arr = []
while k < N:
	n = int(input())
	arr.append(n)
	k = k + 1
print("\n")
for i in range(1, len(arr)):
    x = arr[i] 
    j = i-1
    while j >= 0 and x < arr[j] : 
            arr[j + 1] = arr[j] 
            j =j + 1
    arr[j + 1] = x 
for i in range(len(arr)): 
    print (arr[i]) 






# N = int(input())
# k = 0
# arr = []
# while k < N:
# 	n = int(input())
# 	arr.append(n)
# 	k = k + 1
# print("\n")

# bubble sort
# n=0
# while n<len(number):
#     i=0
#     while i<len(number)-1:
#         if number[i] > number[i+1]:
#             number[i],number[i+1]=number[i+1],number[i]
#         else:
#             number[i],number[i+1]=number[i],number[i+1]
#         i=i+1
#     n=n+1
# t = 0
# while t < len(number):
# 	print(number[t])
# 	t = t + 1 






