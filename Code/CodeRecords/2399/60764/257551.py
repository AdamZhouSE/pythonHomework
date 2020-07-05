import math
T=int(input())
for t in range(T):
    n,m,l,r=map(int,input().split())
    x=list(map(int,input().split()))
    numlist={}
    for i in x:
        if i not in numlist:
            numlist[i]=1
        else:
            numlist[i]+=1
    lrlist=[]
    nlrlist=[]
    n=m+n
    for i in range(l,r+1):
        if i not in numlist:
            numlist[i]=0
        lrlist.append(numlist[i])
    for i in x:
        if i<l or i>r:
            nlrlist.append(numlist[i])
    while m>0:
        lrlist[lrlist.index(min(lrlist))]+=1
        m-=1
    res=1
    for i in lrlist:
        if i>1:
            res*=math.factorial(i)
    for i in nlrlist:
        if i>1:
            res*=math.factorial(i)
    print(int((math.factorial(n)/res)%998244353))