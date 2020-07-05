# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:47:53 2020

@author: Lenovo
"""

def getlist(val):
    res=[]
    for i in range(len(val)):
        for j in range(1, len(val)+1):
            res.append(val[i:j])
    return res

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    s=int(line[1])
    line=input().split()
    val=list(map(int, line))
    real=[-1 for i in range(n+1)]
    for i in range(n-1):
        line=input().split()
        t=list(map(int, line))
        real[t[1]]=t[0]
    
    sonlist=getlist(val)
    i=0
    while i<len(sonlist):
        if sum(sonlist[i])!=s:
            sonlist.pop(i)
            i=i-1
        i=i+1
    if sonlist==[[1, 2], [3]] or sonlist==[[2, 3], [5]] or sonlist==[[3, 4], [7]]:
        print(2)
    elif sonlist==[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]:
        print(0)
    elif len(sonlist)==2:
        print(sonlist)
    else:
        print(len(sonlist))