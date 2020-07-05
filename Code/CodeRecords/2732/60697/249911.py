t=int(input())
a=[]
for i in range(t):
    a.append(list(map(int,input().split(' '))))
for i in range(t):
    base=a[i][0]
    ex=a[i][1]
    mod=a[i][2]
    res=1
    while ex>0:
        if((ex&1)==1):
            res=(res*base)%mod
        base=base*base
        ex>>=1
    print(res)

