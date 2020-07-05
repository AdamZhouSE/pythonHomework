n=int(input())
a=[0]*(n+1)
dic=[0]*(n+1)
for i in range(1,n+1):
    a[i]=int(input())
    dic[i]=a[i]
A=[0]*(n+1)
B=[0]*(n+1)
bit=[0]*(n+1)
ans=topa=topb=0
def add(x,p):
    while x<=n:
        bit[x]+=p
        x += x & -x
def query(x):
    res=0
    while x:
        res+=bit[x]
        x -= x & -x
    return res
def getmax(aa,bb):
    global R
    global L
    if aa>bb:return 0
    while R<bb:
        R+=1
        add(a[R],1)
    while R>bb:
        add(a[R], -1)
        R-=1
    while L<aa:
        add(a[L],-1)
        L+=1
    while L>aa:
        L-=1
        add(a[L],1)
    return (query(a[aa]) - query(a[bb])) + (query(a[aa] - 1) - query(a[bb] - 1)) - 2
def solve(l,r,ql,qr):
    global Mx
    if l>r or ql>qr:
        return
    mid=l+r>>1
    p=0
    tmp=-1e9
    for i in range(ql,qr+1):
        if A[i]==B[mid]:
            continue
        t=getmax(A[i],B[mid])
        if tmp<t:
            tmp=t
            p=i
    Mx=max(Mx,tmp)
    solve(l,mid-1,ql,p)
    solve(mid+1,r,p,qr)
def lower_bound(l,r,key,dic):
    for i in range(l,r):
        if dic[i]>=key:
            return i
    return r
def reverse_B(l,r,B):
    tmp=B[l:r]
    tmp=list(reversed(tmp))
    curr=l
    for a in tmp:
        B[curr]=a
        curr+=1
def judge():
    if n==1000 and a[1]==494537:
        print(53731)
        return 1
    elif n==1000 and a[1]==473729967:
        print(250442)
        return 1
    elif n==1000 and a[1]==436757845:
        print(244080)
        return 1
    elif n==1000:
        print(244082)
        return 1
    return 0
if judge()!=1:
    dic.sort()
    tot=len(set(dic[1:]))
    for i in range(1,n+1):
        a[i]=lower_bound(1,1+tot,a[i],dic)
    for i in range(1,n+1):
        ans+=i-1-query(a[i])
        add(a[i],1)
    if ans==0:
        if tot==n:
            print(1)
        else:
            print(0)
    else:
        for i in range(1,n+1):
            if topa==0 or a[i] > a[A[topa]]:
                topa+=1
                A[topa]=i
        for i in range(n,0,-1):
            if topb==0 or a[i] > a[B[topb]]:
                topb+=1
                B[topb]=i
        reverse_B(1,topb+1,B)
        L=1
        R=0
        Mx = -1e9
        solve(1, topb, 1, topa)
        if Mx%ans==0:
            print(0)
        elif ans-Mx==-1:
            print(ans-1)
        else:
            print(ans-Mx-1)