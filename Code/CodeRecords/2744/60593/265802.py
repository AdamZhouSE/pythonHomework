n=int(input())
N=n*10
p,le,val,bel,h=[0]*N,[0]*N,[0]*N,[0]*N,[0]*N
t,s,sz=[[0]*27 for i in range(N)],['']*(N),0

p[0]=1
for i in range(1,n*10):
    p[i]=p[i-1]*233

for i in range(1,n+1):
    _=list(input().split())
    le[i]=int(_[0])
    s[i]=_[1]
    u,v=0,0
    for j in range(le[i]):
        idd=ord(s[i][j])-ord('a')
        if(not t[u][idd]):
            sz+=1
            t[u][idd]=sz
        u=t[u][idd]
        v=v*233+idd+1
    val[u]+=1
    bel[u]=i
    h[i]=v
res=0
for i in range(1,n+1):
    u=0
    for j in range(le[i]):
        u=t[u][ord(s[i][j])-ord('a')]
        if(val[u] and h[bel[u]]*p[le[i]]+h[i]==h[i]*p[le[bel[u]]]+h[bel[u]]):
            res+=val[u]
print(res*2-n)
