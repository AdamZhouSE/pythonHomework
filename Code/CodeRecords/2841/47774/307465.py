n,m=map(int,input().split(' '))
s=list(map(int,input().split(' ')))
j=0
MAXN = (1<<17)+10
a=[0 for i in range(MAXN)]
ff=[0 for i in range(MAXN<<2)]
sum=[0 for i in range(MAXN<<2)]
n=1<<n
for i in range(1,n+1):
    a[i]=s[j]
    j+=1

def pb(rt):
    if ff[rt]%2==0:
        sum[rt]=sum[rt<<1|1]|sum[rt<<1]
    else:
        sum[rt]=sum[rt<<1|1]^sum[rt<<1]
    
def build(l,r,rt):
    sum[rt]=0
    ff[rt<<1]=ff[rt<<1|1]=0
    if l==r:
        sum[rt]=a[l]
        ff[rt]=-1
        return
    mid=(l+r)>>1
    build(l,mid,rt<<1)
    build(mid+1,r,rt<<1|1)
    ff[rt]=ff[rt<<1]+1
    pb(rt)
    
def update(l,r,p,d,rt):
    if l==r:
        sum[rt]=d
        return
    mid=(l+r)>>1
    if p<=mid:
        update(l,mid,p,d,rt<<1)
    if p>mid:
        update(mid+1,r,p,d,rt<<1|1)
    pb(rt)
    
ff[1]=1
build(1,n,1)
for i in range(1,m+1):
    p,d=map(int,input().split(' '))
    update(1,n,p,d,1)
    print(sum[1])
