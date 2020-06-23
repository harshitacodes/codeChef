# program to print the n finobacci series
def fibonacciSeries(number):
	n1 = 0
	n2 = 1
	sum = 0
	count = 1
	while(count <= number):
	  print(sum)
	  count = count + 1
	  n1 = n2
	  n2 = sum
	  sum = n1 + n2    
userInput = int(input("Enter the number: "))  
fibonacciSeries(userInput)