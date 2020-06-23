# T = int(input())
# a= []
# for i in range(T):
#     b = int(input())
#     a.append(b)
# result = []
# for j in a:
#     set1 = j
#     add = 0
#     for i in range():
#         if set1<=i:
#             add=add+set1
#     if add > 0:
#         maxx = add
#     # print(maxx)
#     result.append(add)
# print(maxx)

# T = int(input())
# a= []
# for i in range(T):
#     b = int(input())
#     a.append(b)
# s_p = sorted(a,reverse = True)
# rev = []
# for i, v in enumerate(s_p):
#     rev.append(i+1*v)
# max(rev)

# output = []
# for j in l:
#     set1 = j
#     sum1 = 0
#     for i in list1:
#         if set1<=i:
#             sum1=sum1+set1
#     output.append(sum1)
# print(max(output))


T = int(input())
l= []
for i in range(T):
    b = int(input())
    l.append(b)
l.sort()
l.reverse()
o = []
j = 0
count = 1
while j < len(l):
    mul = count * l[j]
    o.append(mul)
    j = j + 1
    count=count+1
print(max(o))