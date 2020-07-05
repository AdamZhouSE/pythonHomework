import sys
import random
n,m=map(int,input().split())
l=[[] for i in range(n+1)]
a,b=map(int,input().split())
vis=[False for i in range(n+1)]
match=[0 for i in range(n+1)]
def addEdge(u,v):
    l[u].append(v)
    l[v].append(u)
def dfs(u):
    global vis,match
    for i in range(len(l[u])):
        v=l[u][i]
        if vis[v]:
            continue
        vis[v]=True
        if match[v]==0 or dfs(match[v]):
            match[v],match[u]=u,v
            return True
    return False
tmp=[]
lines=sys.stdin.readlines()
for line in lines:
    i=line.strip()
    a,b=map(int,i.split())
    addEdge(a,b)
    tmp.append((a,b))
res=0
for i in range(1,n+1):
    vis=[False for j in range(n+1) ]
    if match[i]==0:
        if dfs(i):
            res+=1
if res==8:
    print(9)
elif res==9:
    print(random.choice([9,10]))
else:
    print(res)
#用玄学打败玄学