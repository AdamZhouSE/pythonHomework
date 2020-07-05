n,c,m=map(int,input().split(' '))
MAXN=1000
tot=0
rt=[0 for i in range(MAXN)]
ts=pre=rt
ch=[[0 for i in range(2)] for i in range(MAXN*40)]
val=[0 for i in range(MAXN*40)]
def buildt(l,r):
    global tot
    tot+=1
    nd=tot
    if l==r:
        return nd
    mid=(l+r)>>1
    ch[nd][0]=buildt(l,mid)
    ch[nd][1]=buildt(mid+1,r)
    return nd     
def add(rt,l,r,pos,v):
    if (pos==0):
        return rt
    global tot
    tot+=1
    nd=tot
    val[nd]=val[rt]+v
    if (l==r):
        return nd
    mid=(l+r)>>1
    if (pos<=mid):
        ch[nd][0]=add(ch[rt][0],l,mid,pos,v)
        ch[nd][1]=ch[rt][1]
    else:
        ch[nd][1]=add(ch[rt][1],mid+1,r,pos,v)
        ch[nd][0]=ch[rt][0]
    return nd
def query(rt1,rt2,l,r,pl,pr):
    if (pr<l or r<pl):
        return 0
    if (pl<=l and r<=pr):
        return val[rt1]-val[rt2]
    mid=(l+r)>>1;
    return query(ch[rt1][0],ch[rt2][0],l,mid,pl,pr)+query(ch[rt1][1],ch[rt2][1],mid+1,r,pl,pr)
     
rt[0]=buildt(1,c)
tmp=list(map(int, input().split(' ')))
for i in range(1,n+1):
    x=tmp[i-1]
    pre[i]=ts[x];
    ts[x]=i;
    rt[i]=add(rt[i-1],1,c,pre[pre[i]],-1)       
    rt[i]=add(rt[i],1,c,pre[i],1)
for i in range(1,m+1):
    x,y=map(int,input().split(' '))
    print(query(rt[y],rt[x-1],1,c,x,n))
     
     