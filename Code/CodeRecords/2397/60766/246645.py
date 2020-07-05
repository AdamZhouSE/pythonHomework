# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:19:00 2020

@author: Lenovo
"""

limitn=20
limitpoint=1300
n=0
s=[[[0 for i in range(40)] for i in range(20) ] for i in range(5)]
c=[[0 for i in range(4)] for i in range(limitpoint)]
vis=[[0 for i in range(limitpoint)] for i in range(limitpoint)] #boolean
f=[[[0 for i in range(limitpoint)] for i in range(4) ] for i in range(limitpoint)]   #int
best=0

def init():
    global s, n
    n=int(input())
    for k in range(1, 5):
        for i in range(1, n+1):
            for j in range(1, i*2):
                s[k][i][j]=int(input())

def link(a, b):
    global vis
    if vis[a][b]==0:
        vis[a][b]=1
        c[a][0]=c[a][0]+1
        c[a][c[a][0]]=b
    if vis[b][a]==0:
        vis[b][a]=1
        c[b][0]=c[b][0]+1
        c[b][c[b][0]]=a

def make_graph():
    global n, s
    for k in range(1, 5):
        for i in range(2, n):
            for j in range(2, i*2-1):
                link(s[k][i][j], s[k][i][j-1])
                link(s[k][i][j], s[k][i][j+1])
                if j%2==1:
                    link(s[k][i][j], s[k][i+1][j+1])
                else:
                    link(s[k][i][j], s[k][i-1][j-1])
    for k in range(1, 5):
        for j in range(2, n*2, 2):
            link(s[k][n][j], s[k][n][j-1])
            link(s[k][n][j], s[k][n][j+1])
            link(s[k][n][j], s[k][n-1][j-1])
    k=1
    i=1
    while k<=n:
        link(s[1][i][1], s[3][i][i*2-1])
        link(s[1][i][i*2-1], s[2][i][1])
        link(s[2][i][i*2-1], s[3][i][1])
        k=k+1
        i=i+1
    for j in range(1, n*2, 2):
        link(s[1][n][j], s[4][n-(j//2)][1])
        link(s[2][n][j], s[4][j//2+1][((j//2)+1)*2-1])
        link(s[3][n][j], s[4][n][n*2-j])

def tree_max(i, limit1, limit2):
    global c, f
    fro=1
    while c[i][fro]!=limit2:
        fro=fro+1
    if f[i][fro][limit1]>0:
        return f[i][fro][limit1]
    l=0
    r=0
    if limit1>limit2:
        l=limit2+1
        r=limit1
    else:
        l=limit1
        r=limit2-1
    lmax=0
    rmax=0
    for j in range(1, 4):
        if j!=fro and l<=c[i][j] and c[i][j]<=r:
            if c[i][j]<i:
                lmax=max(lmax, tree_max(c[i][j], l, i))
            else:
                rmax=max(rmax, tree_max(c[i][j], r, i))
    f[i][fro][limit1]=lmax+rmax+1
    return f[i][fro][limit1]

def dfs():
    global best, c, n
    best=0
    for i in range(1, n*n*4+1):
        lmax=0
        rmax=0
        for j in range(1, 4):
            if c[i][j]<i:
                lmax=max(lmax, tree_max(c[i][j], 1, i))
            else:
                rmax=max(rmax, tree_max(c[i][j], n*n*4, i))
        best=max(best, lmax+rmax+1)

if __name__ == '__main__':
    init()
    make_graph()
    dfs()
    print(best)