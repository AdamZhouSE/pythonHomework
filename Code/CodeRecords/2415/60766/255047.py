# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 08:44:08 2020
5
5 7 1 2 10
@author: Lenovo
"""

n=0
v=[0 for i in range(39)]
f=[[0 for i in range(47)] for i in range(47)]
i=0
j=0
k=0
ch=[[0 for i in range(49)] for i in range(49)]

def prints(l, r):
    global ch
    if l>r:
        return
    if l==r:
        print(l, end=' ')
        return
    print(ch[l][r], end=' ')
    prints(l, ch[l][r]-1)
    prints(ch[l][r]+1, r)

if __name__ == '__main__':
    n=int(input())
    line=input().split()
    num=list(map(int, line))
    for i in range(1, n+1):
        v[i]=num[i-1]
    for i in range(1, n+1):
        f[i][i]=v[i]
        f[i][i-1]=1
    for i in range(n,0,-1):
        for j in range(i+1,n+1):
            for k in range(i,j+1):
                if f[i][j]<(f[i][k-1]*f[k+1][j]+f[k][k]):
                    f[i][j]=f[i][k-1]*f[k+1][j]+f[k][k]
                    ch[i][j]=k
    print(f[1][n])
    prints(1, n)