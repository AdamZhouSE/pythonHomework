import math
T =int(input())
res=[]
for i in range(T):
    sum=0
    M,N=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    for i in range(M):
        tmp=x[i]
        x[i]=math.log(tmp)/tmp
    for i in range(N):
        tmp=y[i]
        y[i]=math.log(tmp)/tmp
    y.sort()
    for xi in x:
        for yi in y:
            if yi>=xi:
                break
            else:
                sum+=1
    res.append(sum)
for i in range(T):
    print(res[i])
