n,q=map(int,input().split())
son=[[] for i in range(n+1)]
fother=[i for i in range(n+1)]
color=[0 for i in range(n+1)]
color[1]=1
for i in range(n-1):
    u,v=map(int,input().split())
    son[u].append(v)
    fother[v]=u
for i in range(q):
    s=input().split()
    x=int(s[1])
    if s[0]=='C':
        color[x]=1
    else:
        while color[x]==0:
            x=fother[x]
        print(x)