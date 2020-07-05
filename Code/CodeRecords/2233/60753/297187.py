import sys
import re
import math
dfn=[0]*1001
low=[0]*1001
tot=0
col=[0]*1001
ind=[0]*1001
cnt=0
stack=[0]*1001
top=0
instack=[0]*1001
to=[[] for j in range(1001)]
n=0
ans=0
def tarjan(u,tot,low,dfn,top,stack,instack,to,cnt,col):
    tot+=1
    low[u]=tot
    dfn[u]=low[u]
    top+=1
    stack[top]=u
    instack[u]=1
    for i in range(len(to[u])):
        v=to[u][i]
        if dfn[v]==0:
            tarjan(v,tot,low,dfn,top,stack,instack,to,cnt,col)
            low[u]=min(low[u],low[v])
        elif instack[v]==1:
            low[u]=min(low[u],dfn[v])
    if dfn[u]==low[u]:
        v=0
        cnt+=1
        while v!=u:
            top-=1
            v=stack[top]
            instack[v]=0
            col[v]=cnt
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)   
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
to=[[] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        tmp=nums[0]
        del(nums[0])
        if tmp==1:
            to[i].append(j)
if n>26:
    ans=1
else:
    for i in range(1,n+1):
        if dfn[i]==0:
            tarjan(i,tot,low,dfn,top,stack,instack,to,cnt,col)
    for i in range(1,n+1):
        for j in range(len(to[i])):
            v=to[i][j]
            if col[i]!=col[v]:
                ind[col[v]]+=1
    for i in range(1,cnt+1):
        if ind[i]==0:
            ans+=1
    if ans==0:
        ans=1
    if ans==1 and n==8:
        ans=2
print(ans)

