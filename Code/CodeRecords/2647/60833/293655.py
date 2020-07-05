for i in range(0,int(input())):
    n=int(input())
    res=[]
    for j in range(0,n):
        res.append(1)
    k=1
    while(k<=n/2):
        while(res.count(k)>=2):
            res.remove(k)
            res.remove(k)
            res.append(2*k)
        k*=2
    print(len(res))