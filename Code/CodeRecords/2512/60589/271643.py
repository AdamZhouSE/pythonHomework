# 这是一道线段树模版题


'''
update

tr[t].su=tr[t<<1].su+tr[t<<1|1].su
if tr[t].su>=p:
    tr[t].su-=p
'''

np=input().split(' ')
n=int(np[0])
p=int(np[1])
a=input().split(' ')
a=list(map(int,a))
a.insert(0,0)


class kk(object):
    def __init__(self,mu,su,ad):
        self.mu=mu
        self.su=su
        self.ad=ad


tr=[kk(0,0,0) for i in range(len(a)*4)]
op=0
x=0
y=0


def build(t,l,r):
    tr[t].mu=1
    if l==r:
        tr[t].su=a[l]
        return
    mid=l+r>>1
    build(t<<1,l,mid)
    build(t<<1|1,mid+1,r)
    tr[t].su=tr[t<<1].su+tr[t<<1|1].su
    if tr[t].su>=p:
        tr[t].su-=p


build(1,1,n)


def maintain(t,k):
    tr[t << 1].su = (tr[t << 1].su * tr[t].mu + tr[t].ad * (k + 1 >> 1)) % p
    tr[t << 1 | 1].su = (tr[t << 1 | 1].su * tr[t].mu + tr[t].ad * (k >> 1)) % p
    tr[t << 1].mu = tr[t << 1].mu * tr[t].mu % p
    tr[t << 1 | 1].mu = tr[t << 1 | 1].mu * tr[t].mu % p
    tr[t << 1].ad = (tr[t << 1].ad * tr[t].mu + tr[t].ad) % p
    tr[t << 1 | 1].ad = (tr[t << 1 | 1].ad * tr[t].mu + tr[t].ad) % p
    tr[t].mu = 1
    tr[t].ad = 0


def mul(t,l,r,val):
    if x<=l and r<=y:
        tr[t].mu = tr[t].mu * val % p
        tr[t].ad = tr[t].ad * val % p
        tr[t].su = tr[t].su * val % p
        return
    maintain(t, r - l + 1)
    mid = l + r >> 1
    if x<=mid:
        mul(t<<1,l,mid,val)
    if mid<y:
        mul(t<<1|1,mid+1,r,val)
    tr[t].su = tr[t << 1].su + tr[t << 1 | 1].su
    if tr[t].su >= p:
        tr[t].su -= p


def my_add(t,l,r,val):
    if x<=l and r<=y:
        tr[t].ad+=val
        if tr[t].ad>=p:
            tr[t].ad-=p
        tr[t].su = (tr[t].su + (r - l + 1) * val) % p
        return
    maintain(t,r-l+1)
    mid = l + r >> 1
    if x<=mid:
        my_add(t<<1,l,mid,val)
    if mid<y:
        my_add(t<<1|1,mid+1,r,val)
    tr[t].su = tr[t << 1].su + tr[t << 1 | 1].su
    if tr[t].su >= p:
        tr[t].su -= p


def query(t,l,r):
    if x<=l and r<=y:
        return tr[t].su
    maintain(t, r - l + 1)
    mid = l + r >> 1
    ans=0
    if x<=mid:
        ans += query(t << 1, l, mid)
    if mid<y:
        ans += query(t << 1 | 1, mid + 1, r)
    if ans>=p:
        ans-=p
    tr[t].su = tr[t << 1].su + tr[t << 1 | 1].su
    if tr[t].su >= p:
        tr[t].su -= p
    return ans


m=int(input())
for i in range(m):
    action=input().split(' ')
    action=list(map(int,action))
    op=action[0]
    x=action[1]
    y=action[2]
    if op==1:
        mul(1,1,n,action[3])
    if op==2:
        my_add(1,1,n,action[3])
    if op==3:
        print(query(1,1,n))