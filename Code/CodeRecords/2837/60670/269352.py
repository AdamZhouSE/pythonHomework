n,l,r=map(int,input().split())
minn=n-l
t=1
for i in range(0,l):
    minn+=t
    t=t*2
t=1
maxn=0
for i in range(0,r):
    maxn+=t
    t=t*2
maxn+=(n-r)*t
print(str(minn)+" ")