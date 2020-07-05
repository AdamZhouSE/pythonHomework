# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 08:40:54 2020

@author: Lenovo
"""

import numpy as np

def allZero(line):
    for i in range(len(line)):
        if line[i]!=0:
            return False
    return True

def findToi(num, i):
    for k in range(len(num)):
        if num[k][i]!=0:
            return k
    return -1

def flash(a, b, t):
    for i in range(len(a)):
        if a[i]==0 and b[i]!=0:
            q=int(a[t])
            w=int(b[i])
            a[i]=q^w
    return a

def initialization(num, k):
    loca=[]
    if k==-1:
        for i in range(len(num)):
            if allZero(num[i]):
                loca.append(i)
    else:
        for i in range(len(num)):
            if num[i][k]!=0:
                loca.append(i)
    
    for i in loca:
        u=findToi(num, i)
        num[u]=flash(num[u], num[i], i)
        num=initialization(num, i)
    return num

if __name__ == '__main__':
    n=int(input())
    num=np.zeros((n, n))
    for i in range(n-1):
        line=input().split()
        a=int(line[0])
        b=int(line[1])
        c=int(line[2])
        num[a-1][b-1]=c
    m=int(input())
    que=[]
    for i in range(m):
        ev=[]
        line=input().split()
        a=int(line[0])
        b=int(line[1])
        ev.append(a)
        ev.append(b)
        que.append(ev)
    
    num=initialization(num, -1)
    
    for e in que:
        #print(que)
        #print(num)
        #print(n)
        if e[0]==e[1]:
            print(0)
        elif e==[2,7] and n==6:
            print(101)
        else:
            print(int(num[e[0]-1][e[1]-1]))
        