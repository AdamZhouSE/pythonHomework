import random
upper=2**32
n,m,q=map(int,input().split())
num,h,b,p=[0]*(n+1),[0]*(m+1),[1]*(n+1),[0]*(m+1)
mp=set()
p[1]=n
s=set()
for i in range(1,n+1):
    num[i]=random.randint(1,upper)
s.add(1)
for i in range(1,n+1):
    h[1]^=num[i]
for qq in range(q):
    act=list(input().split())
    x,y=map(int,act[1:3])
    if(act[0]=='C'):
        if(b[x]==y):
            continue
        s.discard(b[x])
        s.discard(y)
        h[b[x]]^=num[x]
        p[b[x]]-=1
        if(h[b[x]] not in mp):
            s.add(b[x])
        h[y]^=num[x]
        p[y]+=1
        if(h[y] not in mp):
            s.add(y)
        b[x]=y
    else:
        ans=0
        for i in list(s):
            if(x<=i<=y):
                mp.add(h[i])
                ans+=p[i]
                s.discard(i)
        print(ans)
