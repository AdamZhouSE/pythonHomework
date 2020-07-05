# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:30:36 2020

@author: Lenovo
"""

def column(titable, k):
    count=0
    for i in range(len(titable)):
        if titable[i][k]==1:
            count=count+1
    return count

def init(i, st, ed, titable):
    for k in range(st, ed+1):
        titable[i][k]=1
    return titable

def changemin(num):
    res=[]
    for nu in num:
        res.append((nu//100)*60+(nu%100))
    return res

def printResult():
    n=int(input())
    line=input().split()
    stl=list(map(int, line))
    st=changemin(stl)
    line=input().split()
    enl=list(map(int, line))
    ed=changemin(enl)
    
    N=max(ed)+1
    titable=[[0 for i in range(N)] for i in range(n)]
    
    for i in range(n):
        titable=init(i, st[i], ed[i], titable)
    
    count=0
    for i in range(N):
        count=max(count, column(titable, i))
    print(count)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        printResult()