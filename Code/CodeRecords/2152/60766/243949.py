# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:29:24 2020

@author: Lenovo
"""

import numpy as np

stack=[]
res=[]

def columnnums(num, k):
    count=0
    for ev in num:
        if ev[k]!=0:
            count=count+1
    return count

def getSum(num, k):
    global stack
    if k in stack:
        return 0
    stack.append(k)
    to=k
    for i in range(len(num)):
        if num[k][i]==0 or k==i:
            continue
        else:
            to=i
            break
    return num[k][k]+getSum(num, to)

if __name__ == '__main__':
    n=int(input())
    num=np.zeros((n, n))
    line=input().split()
    for i in range(n):
        num[i][i]=int(line[i])
    line=input().split()
    for i in range(n):
        num[i][int(line[i])-1]=num[int(line[i])-1][int(line[i])-1]
    
    order=[]
    for i in range(1, n+1):
        for j in range(n):
            if columnnums(num, j)==i:
                order.append(j)
    #print(order)
    for i in range(n):
        stack=[]
        res.append(getSum(num, order[i]))
    #print(res)
    for i in range(n):
        print(int(res[order.index(i)]))