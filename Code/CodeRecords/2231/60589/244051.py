t=int(input())
for i in range(t):
    n=int(input())
    factors=[]
    while n>1:
        for p in range(2,n+1):
            if n%p==0:
                factors.append(p)
                n=n//p
                break
    if len(factors)!=3:
        print(0)
    elif len(set(factors))!=3:
        print(0)
    else:
        print(1)