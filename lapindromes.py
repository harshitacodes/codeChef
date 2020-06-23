# T = int(input())
# for i in range(T):
#     s = input()
#     for i in s:
#         if len(s) % 2 ==0:
#             x =  len(s) // 2
#             # print(x)
#             print(y)
#         else:
#             print(i)

T = int(input())
for i in range(T):
    s=list(input())
    l = len(s)
    if(l%2==0):
        s1=s[:l//2] 
        s2=s[l//2:]
    else: 
        s1=s[:l//2]
        s2=s[l//2+1:]
    s1.sort()
    s2.sort()
    if(s1==s2):
        print('YES')
    else: 
        print('NO')



for t_itr in range(0,int(input())):
    s = str(input())
    if s[::-1] == s[]:
        print("YES")
    else:
        print("NO")



for _ in range(int(input())):
    a=input()
    d=dict()
    k=1
    for i in range(0,int(len(a)/2)):
       # print(a[i], a[len(a)-1-i])
        if a[i] not in d:
            d[a[i]]=1
        else:
            d[a[i]]+=1
            
        if a[len(a)-i-1] not in d:
            d[a[len(a)-i-1]]= -1
        else:
            d[a[len(a)-i-1]]+= -1
   # print(d)
    for i in d.values():
           # print(i)
        if(i!=0):
            print("NO")
            k=0
            break
    if(k):
        print("YES")