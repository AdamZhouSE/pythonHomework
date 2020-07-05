from itertools import combinations
t=int(input())
for i in range(t):
    su=[]
    n=int(input())
    for j in range(2,n+1):
        is_su=True
        for x in range(2,j):
            if(j%x==0):
                is_su=False
        if(is_su):
            su.append(j)
    target=list(combinations(is_su,3))
    sp=[]
    for j in target:
        sp.append(j[0]*j[1]*j[2])
    if(n in sp):
        print(1)
    else:
        print(0)
        