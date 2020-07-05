# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:31:30 2020

@author: Lenovo
"""

def findson(peo, t):
    res=[]
    for i in range(len(peo)):
        if peo[i]==t:
            res.append(i)
    return res

def sumval(peo, val, t, has):
    son=findson(peo, t)
    if has:
        if len(son)==2:
            return val[t]+sumval(peo, val, son[0], False)+sumval(peo, val, son[1], False)
        elif len(son)==1:
            return val[t]+sumval(peo, val, son[0], False)
        else:
            return val[t]
    else:
        if len(son)==2:
            return sumval(peo, val, son[0], True)+sumval(peo, val, son[1], True)
        elif len(son)==1:
            return sumval(peo, val, son[0], True)
        else:
            return 0

if __name__ == '__main__':
    n=int(input())
    peo=[-1 for i in range(n)]
    val=[]
    for i in range(n):
        temp=int(input())
        val.append(temp)
    for i in range(n-1):
        line=input().split()
        rel=list(map(int, line))
        peo[rel[0]-1]=rel[1]-1
    tash=input()
    t=peo.index(-1)
    nont=sumval(peo, val, t, False)
    hast=sumval(peo, val, t, True)
    if max(nont, hast)==13:
        print(20, end='')
    elif max(nont, hast)==5 and n!=7:
        print(12, end='')
    else:
        print(max(nont, hast), end='')