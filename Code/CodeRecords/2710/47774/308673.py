N=200000+7
INF=0x3f7f3f7f
l,r=0,0
ans=INF
minv=[0 for i in range(N<<2)]
s=[0 for i in range(3)]
def Update(i,L,R):
    if L==R:
        minv[i]=k
        return
    mid=L+R>>1
    if x<=mid:
        Update(l,L,mid)
    else:
        Update(r,mid+1,R)
    minv[i]=min(minv[l],minv[r])
def Find(i,L,R):
    if minv[i]>k:
        return INF
    elif(L==R):
        return L
    mid=L+R>>1
    if minv[l]<=k:
        return Find(l,L,mid)
    else:
        return Find(r,mid+1,R)
def Query(i,L,R):
    global ans
    if(ql<=L and qr>=R):
        ans=Find(i,L,R)
        return
    mid=L+R>>1
    if(ql<=mid):
        Query(l,L,mid)
        if(ans!=INF):
            return
    if(qr>mid):
        Query(r,mid+1,R)
         
qr,q=map(int,input().split(' '))
n=qr
for i in range(q,0,-1):
    s,k,x=input().split(' ')
    k=int(k)
    x=int(x)
    if s=='M':
        Update(1,1,n)
    else:
        ql=x
        ans=INF
        Query(1,1,n)
        if ans==INF:
            print(-1)
        else:
            print(ans)