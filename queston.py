nlist=[[24, 33, 44, 5, 21, 19, 23, 30],[1 , 4, 3, 5, 9],[34,78,56,34,]]
print("unsorted list:",nlist)
for j in range (len(nlist)-1,0,-1):
	for i in range (j):
		if nlist[i][j]>nlist[i][j+1]:
			nlist[i][j],nlist[i][j+1]=nlist[i][j+1],nlist[i][j]
			list2=nlist
	else:
		list1=nlist
print("sorted list:",nlist)
 

nlist=[[24, 33, 44, 5, 21, 19, 23, 30],[1 , 4, 3, 5, 9],[34,78,56,34,]]
print("unsorted list:",nlist)
i = 0
while i < len(nlist):
	j = 0
	while j <len(nlist[i]):
		if nlist[i][j]>nlist[i][j+1]:
			nlist[i][j],nlist[i][j+1]=nlist[i][j+1],nlist[i][j]
			list2=nlist
	else:
		list1=nlist
print("sorted list:",nlist)
 

num_list=[24, 33, 44, 5, 21, 19, 23, 30]
print("unsorted list:",num_list)
for j in range (len(num_list)-1,0,-1):
	for i in range (j):
		if num_list[i]>num_list[i+1]:
			num_list[i],num_list[i+1]=num_list[i+1],num_list[i]
			list2=num_list
	else:
		list1=num_list
print("sorted list:",num_list)



num_list=[24, 33, 44, 5, 21, 19, 23, 30]
i = 0
while i < len(num_list):
	j = 0
	while j < len(num_list) - 1:
		if num_list[i][j] > num_list[i][j+1]:
			num_list[i][j],num_list[i][j+1]=num_list[i][j+1],num_list[i][j]
		else:
			num_list[i][j],num_list[i][j+1]=num_list[i][j],num_list[i][j+1]
		j = j + 1
	i = i + 1	
print(num_list)		

number = [24, 33, 44, 5, 21, 19, 23, 30]
print("unsorted list:",number	)
n = 0 
while n<len(number):
    i=0
    while i<len(number)-1:
        if number[i] > number[i+1]:
            number[i],number[i+1]=number[i+1],number[i]
        else:
            number[i],number[i+1]=number[i],number[i+1]
        i=i+1
    n=n+1
print(number)

nlist=[[24, 33, 44, 5, 21, 19, 23, 30],[1 , 4, 3, 5, 9],[34,78,56,34,]]
j=0
while j < len(nlist):
	n=0
	while n < len(nlist[j]):
	 	i=0
	 	while i < len(nlist[j])-1:
	 	 	if nlist[j][i] > nlist[j][i+1]:
	 	 		nlist[j][i],nlist[j][i+1] =  nlist[j][i+1],nlist[j][i]
	 	 	i=i+1
	 	n=n+1
	j=j+1
print(nlist)


def sort_the_list(number):
	print("unsorted list", nlist)
	j=0
	while j < len(nlist):
		n=0
		while n < len(nlist[j]):
		 	i=0
		 	while i < len(nlist[j]):
		 		a = nlist[j][i]
				b = nlist[j][i+1]
				if a > b:
					c = a
					a = b
					b = c
		 	 	i=i+1
		 	n=n+1
		j=j+1
	return nlist	
nlist=[[24, 33, 44, 5, 21, 19, 23, 30],[1 , 4, 3, 5, 9],[34,78,56,34,]]		
print(sort_the_list(nlist))


my_list = [[-15, -26, 15, 1, 23, -64, 23, 76],[24, 33, 44, 5, 21, 19, 23, 30],[1 , 4, 3, 5, 9]]
new_list = []
final_list = []
while my_list:
	i = 0
	while i < len(my_list[i]):
	    min = my_list[i][0]  
	    for x in my_list: 
	        if x < min:
	            min = x
	    new_list.append(min)
	    my_list.remove(min) 
	    i = i + 1  
	final_list.append(new_list)     

print(new_list)

# To print the sorted nested list without using sort funtion
def sorttheList(myList):
	newList = []
	while myList:
	    minimum = myList[0]  
	    for x in myList: 
	        if x < minimum:
	            minimum = x
	    newList = newList + [minimum]
	    myList.remove(minimum) 
	return newList     
unsortedList = [[-15,-26,5,1,23,-64,23,76],[12,13,7,45,6,1,0],[89,56,23,13,8]]     
sortedList = []

for oneList in unsortedList:
	anotherSortedlist = sorttheList(oneList)
	sortedList = sortedList + [anotherSortedlist]

print(sortedList)

def sort_the_list(number):
	print("unsorted list", nlist)
	j=0
	while j < len(nlist):
		n=0
		while n < len(nlist[j]):
		 	i=0
		 	while i < len(nlist[j])-1:
		 		if nlist[j][i] > nlist[j][i+1]:
		 			nlist[j][i],nlist[j][i+1] = nlist[j][i+1],nlist[j][i]
		 		i=i+1
		 	n=n+1
		j=j+1
	return nlist	
nlist=[[24, 33, 44, 5, 21, 19, 23, 30],[1 , 4, 3, 5, 9],[34,78,56,34,]]		
print(sort_the_list(nlist))


to print the fabonacci series
Python program to generate Fibonacci series until 'n' value
n = int(input("Enter the number: "))
def fibonacciSeries(number):
	a = 0
	b = 1
	sum = 0
	count = 1
	while(count <= number):
	  print(sum)
	  count = count + 1
	  a = b
	  b = sum
	  sum = a + b    
userInput = int(input("Enter the number: "))  
fibonacciSeries(userInput)



nterms = int(input("How many terms? "))
n1 = 0 
n2 = 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   # print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   # print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


A simple Python 3 program 
to find three elements 
whose sum is equal to  
given sum 
  
Prints all triplets in 
arr[] with given sum 
def findTriplets(arr, n, sum): 
  
    for i in range(0 , n - 2):  
        for j in range(i + 1 , n - 1):  
            for k in range(j + 1, n): 
                if (arr[i] + arr[j] + 
                    arr[k] == sum):  
                    print(arr[i], " ",  
                          arr[j] ," ",  
                          arr[k] , sep = "") 
              
# Driver code 
arr = [ 2, 3, 4, 5, 7 ] 
n = len(arr)  
findTriplets(arr, n, 5) 
  
def findTriplet(arr, n): 
      
    # sort the array 
    arr.sort() 
   
    # for every element in arr 
    # check if a pair exist(in array) whose 
    # sum is equal to arr element 
    i = n - 1
    while(i >= 0): 
        j = 0
        k = i - 1
        while (j < k): 
            if (arr[i] == arr[j] + arr[k]): 
                 
                # pair found 
                print "numbers are ", arr[i], arr[j], arr[k] 
                return
            elif (arr[i] > arr[j] + arr[k]): 
                j += 1
            else: 
                k -= 1
        i -= 1
          
    # no such triplet is found in array 
    print("No such triplet exists")
   
# driver program 
arr = [ 5, 32, 1, 7, 10, 50, 19, 21, 2 ] 
n = len(arr) 
findTriplet(arr, n) 


word="I am a girl cd ef" #word = "1"
count=1
length=""
if len(word)>1:
    for i in range(1,len(word)):
       if word[i-1]==word[i]:
          count+=1
       else :
           length += word[i-1]+" repeats "+str(count)+", "
           count=1
    length += ("and "+word[i]+" repeats "+str(count))
else:
    i=0
    length += ("and "+word[i]+" repeats "+str(count))
print (length)




a = [2,3,4,5,6,7]
a + b = c