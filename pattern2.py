# program to print the pattern of the number
i = 5
b = 0
# logic of loop
while i <= 25:
    a = i
    while a > b:
        print(a, end = "")
        a = a - 1
    # will giive one new line 
    print("\n")
    b=i
    # increment of 5
    i = i + 5