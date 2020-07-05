import math
T=int(input())
for t in range(T):
    n,m,l,r=map(int,input().split())
    x=list(map(int,input().split()))
    numlist={}
    res=1
    n=n+m
    for i in x:
        if i not in numlist:
            numlist[i]=1
        else:
            numlist[i]+=1
    for i in range(l,r+1):
        if i not in numlist and m>0:
            numlist[i]=1
            m-=1
    while m>0:
        min=l
        for i in range(l,r+1):
            if numlist[i]<numlist[min]:
                min=i
        numlist[min]+=1
        m-=1
    for key in numlist:
        if numlist[key]>1:
            res*=math.factorial(numlist[key])
    print(int((math.factorial(n)/res)%998244353))