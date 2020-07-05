nn=int(input())
for p in range(nn):
    a=int(input())
    n=1
    res=""
    kk=a
    while a>0:
        if n%2==0:
            a=a-1
            res=res+str(n//2)+" "
        else:
            a=a-n//2-1
            for s in range(n//2+1):
                res=res+str(kk)+" "
                kk -= 1
        n=n+1
    a=[""]
    b=[""]
    for r in range(len(a)):
        if res==a[i]:
            res=b[i]
    print(res)