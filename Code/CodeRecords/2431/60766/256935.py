# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:45:26 2020
https://www.cnblogs.com/ukcxrtjr/p/11184592.html
@author: Lenovo
"""

import math

class Node:
    u=0
    v=0
    w=0

        
N=100000
s=0
u1=0
v1=0
Cnt=0
fa=[0 for i in range(N)]
ans=0
x=[0 for i in range(N)]
y=[0 for i in range(N)]
p=0
cou=0
Edge=[]

def findEdge():
    global Edge, N
    for i in range(2*N):
        nl=Node()
        Edge.append(nl)

def find(x):
    global fa
    if fa[x]!=x:
        fa[x]=find(fa[x])
    return fa[x]

def kruskal():
    global Edge, p, s, fa, Cnt, cou, ans
    l=[]
    l.append(Edge[0])
    r=Edge[1+cou:]
    Edge=sorted(Edge[1:1+cou], key=lambda x: (x.w))
    Edge=l+Edge+r
    
    for i in range(1, cou+1):
        u1=find(Edge[i].u)
        v1=find(Edge[i].v)
        if u1==v1:
            continue
        ans=Edge[i].w
        fa[v1]=u1
        Cnt=Cnt+1
        if Cnt==p-s:
            break


if __name__ == "__main__":
    line=input().split()
    s=int(line[0])
    p=int(line[1])
    findEdge()
    for i in range(1, p+1):
        line=input().split()
        x[i]=int(line[0])
        y[i]=int(line[1])
        for j in range(1, i):
            d=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])
            cou=cou+1
            Edge[cou].u=i
            Edge[cou].v=j
            Edge[cou].w=d
    
    for i in range(1, p+1):
        fa[i]=i
    kruskal()
    print('{:.2f}'.format(math.sqrt(ans)), end='')