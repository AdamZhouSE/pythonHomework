# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:19:14 2020

@author: Lenovo
"""

def toSum(num, i, j, ev):
    nu=0
    for t in range(i, i+ev):
        for r in range(j, j+ev):
            nu=nu+num[t][r]
    return nu

def getminSum(num, ev):
    if ev==1:
        return getMin(num)
    count=9999999999999
    for i in range(len(num)-ev+1):
        for j in range(len(num[0])-ev+1):
            count=min(count, toSum(num, i, j, ev))
    return count

def Test(num, ta, limit):
    for i in range(limit):
        edge=limit-i
        mSum=getminSum(num, edge)
        if mSum<=ta:
            print(edge)
            break

def getMin(num):
    count=num[0][0]
    for i in range(len(num)):
        for j in range(len(num[0])):
            count=min(count, num[i][j])
    return count

if __name__ == "__main__":
    n=int(input())
    num=[]
    for i in range(n):
        line=input().split(',')
        temp=list(map(int, line))
        num.append(temp)
    ta=int(input())
    limit=min(n, len(num[0]))
    if getMin(num)>ta:
        print(0)
    elif getMin(num)==ta:
        print(1)
    else:
        Test(num, ta, limit)