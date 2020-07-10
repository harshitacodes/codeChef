N= int(input())
l=list(map(int,input().split()))
lucky=0
unlucky=0
i = 0
while i < len(l):
    if i%2==0:
        lucky=lucky + 1
    else:
        unlucky=unlucky + 1
    i = i + 1    
if lucky>unlucky:
    print("READY FOR BATTLE")
else:
    print("NOT READY")      

