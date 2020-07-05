n = int(input())
dad=[i for i in range(n+1)]
dist=[0]*(n+1)


def getdad(i):
    if dad[i]!=i:
        last=dad[i]
        dad[i]=getdad(dad[i])
        dist[i]+=dist[last]
    return dad[i]
ans=10000000
def check(a,b):
    global ans
    x=getdad(a)
    y=getdad(b)
    if x!=y:
        dad[x]=y
        dist[a]=dist[b]+1
    else:
        ans=min(ans,dad[a]+dad[b]+1)

src=[int(x) for x in input().split()]
for i in range(n):
    a=getdad(i+1)
    b=getdad(src[i])
    if a!=b:
        dad[a]=b
        dist[i+1]=dist[src[i]]+1
    else:
        ans=min(ans,dist[i+1]+dist[src[i]]+1)
print(ans,end='')
    