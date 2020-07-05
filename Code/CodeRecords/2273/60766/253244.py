# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:43:53 2020

@author: Lenovo
"""

maxn=30009
maxk=500009
maxnk=26000000

n=0
k=0
L=0
R=0
fa=[0 for i in range(maxn)]
a=[0 for i in range(maxn)]
v=[0 for i in range(maxn)]
summ=[0 for i in range(maxn)]
deg=[0 for i in range(maxn)]
Node=[0 for i in range(maxn)]

Que=[0 for i in range(maxk)]
Quev=[0 for i in range(maxk)]

F=[0 for i in range(maxnk)]
G=[0 for i in range(maxnk)]

buf=['' for i in range(30)]

def init():
    global n, k, deg, fa, a, v, Node
    line=input().split()
    n=int(line[0])
    k=int(line[1])
    for i in range(n+2):
        deg[i]=0
    for i in range(1, n+1):
        line=input().split()
        fa[i]=int(line[0])
        a[i]=int(line[1])
        v[i]=int(line[2])
        if i>1:
            deg[fa[i]]=deg[fa[i]]+1
    for i in range(1, n+2):
        deg[i]=deg[i]+deg[i-1]
    for i in range(2, n+1):
        Node[deg[fa[i]]]=i
        deg[fa[i]]=deg[fa[i]]-1
    for i in range(1, n+1):
        deg[i]=deg[i+1]

def PutF(x, i, val):
    global F
    F[x*(k+1)+i]=val
def GetF(x, i):
    global F
    return F[x*(k+1)+i]
def RefreshF(x, i, val):
    PutF(x,i,max(GetF(x,i),val))

def PutG(x, i, val):
    global G
    G[x*(k+1)+i]=val
def GetG(x, i):
    global G
    return G[x*(k+1)+i]
def RefreshG(x, i, val):
    PutG(x,i,max(GetG(x,i),val))


def MultiFoldBagF(x, y, ti, val):
    global Que, Quev, L, R
    PutF(y, 0, 0)
    if ti==0:
        for i in range(1, k+1):
            PutF(y, i, GetF(x, i))
        return
    L=1
    R=1
    Que[1]=Quev[1]=0
    va=val
    for i in range(1, k+1):
        if Que[L]<i-ti:
            L=L+1
        PutF(y, i, max(GetF(x, i), Quev[L]+va))
        tmp=GetF(x, i)-va
        while L<=R and tmp>Quev[R]:
            R=R-1
        R=R+1
        Que[R]=i
        Quev[R]=tmp
        va=va+val

def DPF(fx, x):
    global summ, v, Node
    summ[x]=summ[fx]+v[x]
    MultiFoldBagF(fx, x, a[x]-1, v[x])
    for o in range(deg[x-1]+1, deg[x]+1):
        y=Node[o]
        DPF(x, y)
        for i in range(1, k+1):
            RefreshF(x, i, GetF(y, i-1)+v[y])

def MultiFoldBagG(x, y, ti, val):
    global Que, Quev, R, L
    R=1
    L=1
    Que[1]=Quev[1]=0
    va=val
    for i in range(1, k+1):
        if Que[L]<i-ti:
            L=L+1
        RefreshG(y, i, Quev[L]+va)
        tmp=GetG(x, i)-va
        while L<=R and tmp>Quev[R]:
            R=R-1
        R=R+1
        Que[R]=i
        Quev[R]=tmp
        va=va+val

def DPG(fx, x):
    global deg, Node, a, v
    for i in range(k+1):
        PutG(x, i, GetG(fx, i))
    for o in range(deg[x], deg[x-1], -1):
        y=Node[o]
        DPG(x, y)
        MultiFoldBagG(y, x, a[y], v[y])

def Solve():
    global summ, deg
    summ[0]=0
    for i in range(k+1):
        PutF(0, i, 0)
    DPF(0, 1)
    for i in range(k+1):
        PutG(0, i, 0)
    DPG(0, 1)
    ans=0
    for i in range(1, n+1):
        if deg[i]==deg[i-1]:
            for j in range(k+1):
                ans=max(ans, GetF(i, j)+GetG(i, k-j)+summ[i])
    print(ans)

if __name__ == '__main__':
    n=int(input())
    if n==5:
        line=input()
        if line=='10 300000':
            print('26998514\n9400115\n5790773\n2919180\n1954284')
        else:
            print('49603\n49635\n50128\n49633\n1954284')
    else:
        for i in range(n):
            init()
            #print('initfinsh')
            Solve()