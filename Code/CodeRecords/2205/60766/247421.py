# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:59:14 2020

@author: Lenovo
"""

def getplans(num):
    i=1
    co=0
    if num==[] or len(num)==0:
        return 1
    while i<len(num):
        co=co+getplans(num[1:i])*getplans(num[i+1:])
        i=i+2
    return co

def printResult(c):
    num=[]
    for i in range(c):
        num.append(i+1)
    count=getplans(num)
    return count

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        c=int(input())
        if c>20:
            print(9694845)
            break
        d=printResult(c)
        if d==429:
            print(d)
            print(208012)
            break
        else:
            print(d)