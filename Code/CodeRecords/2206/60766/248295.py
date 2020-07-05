# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:51:32 2020

@author: Lenovo
"""

def getadds(n):
    i=0
    t=1
    for k in range(n):
        i=i+t
        t=t+1
    res=1
    for k in range(t-1):
        res=res*i
        i=i-1
    #print(res)
    return res

def getResult(n):
    res=0
    for i in range(1, n+1):
        res=res+getadds(i)
    return res

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        nu=int(input())
        r=getResult(nu)
        print(r)