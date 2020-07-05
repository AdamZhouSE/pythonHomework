def x(n):
    if n==0:
        return 0
    if n=1:
        return 1
    if n==2:
        return 2
    if n%2==0:
        return x(n-1)+1
    else:
        return x(n-1)+n//2
nn=int(input())
for p in range(nn):
    a=int(input())
    n=1
    res=""
    k=a
    kk=a
    while k>0:
        k=a-x(n)
        if n%2==0:
            res=res+str(n//2)+" "
        else:
            for s in range(n//2):
                res=res+str(kk)+" "
                kk -= 1
    print(res)