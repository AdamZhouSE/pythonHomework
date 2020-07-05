import math
t=int(input())
for i in range(0,t):
    a=input().split()
    n=int(a[0])
    l=int(a[1])
    r=int(a[2])
    res=[]
    k=0
    while n!=0:
        k=n%2
        n=int(n/2)
        res=res+[k]
   
    for j in range(l-1,r):
        if res[j]==1:
            res[j]=0
        else:
            res[j]=1
    p=[]
    for j in range(0,len(res)):
        p=[res[j]]+p
    ans=0

    for j in range(0,len(p)):
        ans=ans+int(math.pow(2,len(p)-j-1))*p[j]
    print(ans)
