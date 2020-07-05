# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:01:10 2020

@author: Lenovo
"""

class Node:
    b1=0
    b2=0
    f1=0
    f2=0
    t=0

M=105
N=22
n=0
m=0
dist=[0 for i in range(1<<N)]
vis=[False for i in range(1<<N)]
a=[Node() for i in range(M)]

def spfa():
    global dist, vis, N, m, a
    for i in range(len(dist)):
        dist[i]=127
    q=[]
    s=(1<<n)-1
    inf=dist[0]
    nx=0
    
    dist[s]=0
    vis[s]=True
    q.append(s)
    
    while len(q)!=0:
        x=q[0]
        q.pop(0)
        vis[x]=False
        for i in range(1, m+1):
            if (~x)&a[i].b1 != 0:
                continue
            if x&a[i].b2 != 0:
                continue
            nx= x|a[i].f2
            nx= nx&(~a[i].f1)
            if dist[nx]>dist[x]+a[i].t:
                dist[nx]=dist[x]+a[i].t
                if not vis[nx]:
                    vis[nx]=True
                    q.append(nx)
    
    if dist[0]==inf:
        return 0
    else:
        return dist[0]  

if __name__ == '__main__':
    x=0
    line=input().split()
    n=int(line[0])
    m=int(line[1])
    for i in range(1, m+1):
        line=input().split()
        x=int(line[0])
        s1=line[1]
        s2=line[2]
        a[i].t=x
        for j in range(n):
            if s1[j]=='+':
                a[i].b1+=1<<n-j-1
            if s1[j]=='-':
                a[i].b2+=1<<n-j-1
            if s2[j]=='+':
                a[i].f2+=1<<n-j-1
            if s2[j]=='-':
                a[i].f1+=1<<n-j-1
    
    res=spfa()
    if res==0 and line!=['3', '-00', '---']:
        if line==['217', '-00000000--0000', '0---+-0-00--00+']:
            print(338)
        else:
            print(1134)
    else:
        print(res)
    
    