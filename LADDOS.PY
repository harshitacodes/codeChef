T = int(input())
for i in range(T):
    act,origin = input().split()
    act = int(act)
    laddo = 0
    rem = 0
    for j in range(act):
        n = list(input().split())
        if len(n) == 1:
            if (n[0]=='TOP_CONTRIBUTOR'):
                laddo = laddo + 300
            else:
                laddo = laddo + 50
        else:
            if (n[0]=='CONTEST_WON'):
                if int(n[1])<=20:
                    laddo = laddo + 300 + (20-int(n[1]))
                else:
                    laddo = laddo + 300
            else:
                laddo = laddo + int(n[1])
    print(laddo)
    if(origin=='INDIAN'):
        rem=laddo//200
        print(rem)
    else:
        rem=laddo//400
        print(rem)