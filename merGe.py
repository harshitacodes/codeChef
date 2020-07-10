def merge(left, right):
    left_length = len(left)
    right_length = len(right)
 
    array = []
    i = 0
    j = 0
 
    while i < left_length and j < right_length:
        if left[i] < right[j]:
            array.append(left[i])
            i =i + 1
        else:
            array.append(right[j])
            j = j + 1
    # print(array)
    while i < left_length:
        array.append(left[i])
        i += 1
 
    while j < right_length:
        array.append(right[j])
        j += 1
 
    return array
 
def merge_sort(array):
    length = len(array)
 
    # base case
    if length <= 1:
        return array

    # recursion
    midpoint = length // 2
    left_half = merge_sort(array[:midpoint])
    right_half = merge_sort(array[midpoint:])
    return merge(left_half, right_half)
 

# print("Initial array:", array)
N = int(input())
k = 0
array = []
while k < N:
	n = int(input())
	array.append(n)
	k = k + 1
# print("\n")
# print("Sorted array:", merge_sort(array))
for l in merge_sort(array):
    print(l)