import ipdb; ipdb.set_trace()
def function(half,number):
	if half*half >number:
		half = half-0.1
	elif half*half< number:
		return half
	else:
		return function(half,number)



number  = int(input("Enter the Number To get the Square Root"))
start = 0
end = number
m = 0
min_range = 0.0000000001

while end-start > min_range:
	half = (start+end)/2.0
	doubl = half*half
	if abs(doubl-number) <= min_range:
		half = half
		break
	elif doubl<number:
		start = half
	else:
		end = half
print (half)
