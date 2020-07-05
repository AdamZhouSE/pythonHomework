nn=int(input())
for p in range(nn):
    a=int(input())
    n=1
    res=""
    kk=a
    while a>0:
        a=a-x(n)
        if n%2==0:
            res=res+str(n//2)+" "
        else:
            for s in range(n//2):
                res=res+str(kk)+" "
                kk -= 1
        n=n+1
    print(res)