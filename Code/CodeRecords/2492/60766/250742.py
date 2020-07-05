# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:20:39 2020

@author: Lenovo
"""

import copy

ma=[[0 for i in range(1000)] for i in range(1000)]
su=copy.deepcopy(ma)

def come():
    line=input().split()
    c=int(line[0])
    n=int(line[1])
    N=0
    M=0
    for i in range(1, n+1):
        line=input().split()
        x=int(line[0])
        y=int(line[1])
        ma[x][y]=ma[x][y]+1
        N=max(N, x)
        M=max(M, y)
    maxn=max(N, M)
    for i in range(1, maxn+1):
        for j in range(1, maxn+1):
            su[i][j]=su[i-1][j]+su[i][j-1]+ma[i][j]-su[i-1][j-1]
    for i in range(1, maxn+1):
        for j in range(i, maxn+1):
            for k in range(i, maxn+1):
                if su[j][k]-su[j-i][k]-su[j][k-i]+su[j-i][k-i]>=c:
                    print(i)
                    return

if __name__ == '__main__':
    come()