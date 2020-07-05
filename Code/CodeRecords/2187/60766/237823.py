# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:24:31 2020

@author: Lenovo
"""

def summation(num, i, k):
    su=0
    for j in range(i, i+k):
        su=su+num[j]
    return su

def printMaxSub():
    line=input().split()
    n=int(line[0])
    k=int(line[1])
    line=input().split()
    num=list(map(int, line))
    res=0
    
    for i in range(n-k+1):
        res=max(res, summation(num, i, k))
    print(res)
    

if __name__ == '__main__':
    n=int(input())
    
    for i in range(n):
        printMaxSub()
