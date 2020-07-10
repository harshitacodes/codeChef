N = int(input())
i = 0
while i < N:
    n= int(input())
    a = 2
    sum = 0
    while a * a <= n:
    	if n % a == 0:
    		if a == n/a:
    			sum = sum + a
    		else:
    			sum = sum + a + n/a
    	a = a + 1
    else:
    	sum = sum + 1
    	if sum == 1:
    	    print("NO")
    	elif sum == n:
    		print("YES")
    	else:
    		print("NO")					
    i = i + 1
