# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:15:12 2020

@author: Lenovo
"""

maxn=100050
n=0
f=[0 for i in range(maxn)]
d=[0 for i in range(maxn)]
ind=[0 for i in range(maxn)]
mintree=[0 for i in range(maxn)]
now=[0 for i in range(maxn)]
ans=0

def read():
    global n, f, d, ind, mintree
    n=int(input())
    for i in range(1, n+1):
        line=input().split()
        f[i]=int(line[0])
        d[i]=int(line[1])
        mintree[i]=int(line[2])
        if f[i]!=-1:
            ind[f[i]]=ind[f[i]]+1

def work():
    global n, f, d, ind, mintree, now, ans
    q=[]
    for i in range(1, n+1):
        if ind[i]==0:
            q.append(i)
    while len(q)!=0:
        t=q[0]
        if d[t]>now[t]:
            ans+=mintree[t]*(d[t]-now[t])
        if t!=1:
            mintree[f[t]]=min(mintree[f[t]], mintree[t])
            ind[f[t]]=ind[f[t]]-1
            now[f[t]]+=max(d[t],now[t])
            if ind[f[t]]==0:
                q.append(f[t])
        q.pop(0)
    
def prints():
    print(ans)            

if __name__ == '__main__':
    read()
    work()
    prints()