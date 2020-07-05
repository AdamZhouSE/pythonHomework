def Update(i,L,R):
    global k,X
    if(L==R):
        minv[i]=k
        return
    mid=(L+R)>>1
    if(x<=mid):
        Update(i<<1,L,mid)
    else:
        Update(i<<1|1,mid+1,R)
    minv[i]=min(minv[i<<1],minv[i<<1|1])
def find(i,L,R):
    global k
    if(minv[i]>k):
        return 2**31
    elif(L==R):
        return L
    mid=(L+R)>>1
    return find(i<<1,L,mid) if minv[i<<1]<=k else find(i<<1|1,mid+1,R)
def Query(i,L,R):
    global ql,qr,ans
    if(ql<=L and qr>=R):
        ans=find(i,L,R)
        return
    mid=(L+R)>>1
    if(ql<=mid):
        Query(i<<1,L,mid)
        if(ans!=2**31):
            return
    if(qr>mid):
        Query(i<<1|1,mid+1,R)
n,q=map(int,input().split())
qr,ql,k,x=n,0,0,0
minv=[2**31]*(n<<2)
for qq in range(q):
    act=list(input().split())
    k=int(act[1])
    if(act[0]=='M'):
        x=int(act[2])
        Update(1,1,n)
    else:
        ql=int(act[2])
        ans=2**31
        Query(1,1,n)
        print(-1 if ans==2**31 else ans)
