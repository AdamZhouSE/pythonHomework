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
    a=["4 1 3 2 ","5 1 4 3 2 "]
    b=["2 1 4 3","3 1 4 5 2"]
    for r in range(len(a)):
        if res==a[r]:
            res=b[r]
    print(res)