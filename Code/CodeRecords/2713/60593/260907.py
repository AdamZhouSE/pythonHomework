N=5*(10**5)+100
n,m=map(int,input().split())
aa=list(map(int,input().split()))
a,L,R=[0]*N,[0]*N,[0]*N
mx,mn=0,N
Q=[]
flag=True
for i in range(1,n+1):
    a[i]=aa[i-1]
    mx=max(mx,a[i])
    mn=min(mn,a[i])
for i in range(n,0,-1):
    if(not R[a[i]]):
        R[a[i]]=i
for i in range(1,n+1):
    if(not L[a[i]]):
        L[a[i]]=i
for i in range(1,n+1):
    if(not a[i]):
        if(mx<m):
            a[i]=m
            mx=m
        elif(len(Q)):
            a[i]=Q[len(Q)-1]
        else:
            a[i]=1
    else:
        if(L[a[i]]==i and L[a[i]]<R[a[i]]):
            if(a[i] not in Q):
                Q.append(a[i])
        if(R[a[i]]==i and L[a[i]]<R[a[i]]):
            Q.remove(a[i])
        if(len(Q)):
            if(a[i]<Q[len(Q)-1]):
                flag=False
                break
if(mx<m or not flag):
    print('NO')
else:
    print('YES')
    for i in range(1,n+1):
        print(a[i],end=' ') 
