N = int(input())
i = 0
while i < N:
	(n1, n2, n3) = map(int, input().split())
	if (n1>n2):
	    if(n1>n3):
	        print(n1)
	    else:
	        print(n3)
	elif(n2>n3):
	    print(n2)
	else:
	    print(n3)
	i = i + 1