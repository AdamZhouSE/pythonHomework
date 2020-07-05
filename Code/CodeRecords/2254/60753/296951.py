import sys
import re
import math
counts=0
index=0
head=[0]*1010
nexts=[0]*100010
ver=[0]*100010
dfn=[0]*1010
low=[0]*1010
belong=[0]*1010
cnt=0
indegree=[0]*1010
xxx=[0]*1010
father=[0]*1010
sign=[0]*1010
vis=[0]*1010
tot=0
stack=[]
def add(x,y):
    ver[index]=y
    xxx[index]=x
    nexts[index]=head[x]
    head[x]=index
    sign[index]=counts
def tarjan(x):
    tot+=1
    low[x]=tot
    dfn[x]=low[x]
    stack.append(x)
    vis[x]=1
    i=head[x]
    while i!=0:
        y=ver[i]
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)   
nums= [int(e) for e in digits ]
f=nums[0]
del(nums[0])
r=nums[0]
del(nums[0])
for i in range(r):
    x=nums[2*i]
    y=nums[2*i+1]
    counts+=1
    index+=1
    add(x,y)
    index+=1
    add(y,x)
    father[x]=y
    father[y]=x
for i in range(f):
    if belong[i]==0:
        tarjan(i)