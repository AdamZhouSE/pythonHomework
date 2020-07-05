u=int(input())
for p in range(u):
    n=int(input())
    d=n
    res=""
    ans=-5
    while 1:
        res=res+str(n)+" "
        n+=ans
        if(n<=0):
            ans=5
        if(d==n):
            res = res + str(n) + " "
            break
    print(res)