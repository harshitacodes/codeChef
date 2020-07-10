t=int(input())
for i in range(t):
    
 c,d,l = map(int,input().split())
 maximum=d*4
 if l<4:
     print("no")
 elif l%4!=0:
     print("no")
 elif l>4*d+4*c:
     print("no")
 elif l<4*d:
     print("no")
 elif c<d*2:
     if maximum==l:
         print("yes")
     for i in range(c):
        maximum=maximum+4
        if maximum==l:
            print("yes")
            
 elif c>d*2:
     a=c-(d*2)
     b=c-a
     a=4*a 
     maximum=maximum+a
     if maximum==l:
         print("yes")
     for i in range(b):
      maximum=maximum+4
      if maximum==l:
         print("yes")
         
 else:
     print("no")



t=int(input())
for i in range(t):
    c,d,l=map(int,input().split())
    s=c+d
    mc=s*4
    # print(mc)
    if c<=2*d:
        m=d*4
    else:
        a = c-2*d
        m=d*4 +a*4
        # print(m)
        print(m)
    if l>=m and l<=mc and l%4==0:
        print("yes")
    else:
        print("no")
            


