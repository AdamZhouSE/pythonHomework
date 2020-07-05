# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:23:53 2020

@author: Lenovo
"""

def printResult(num, x):
    count=[]
    for i in num:
        if i%x==0:
            count.append(i)
    if len(count)==0:
        print(0)
        return
    elif len(count)==1:
        print(count[0])
        return
    else:
        t=0
        for g in count:
            t=t | g
        print(t)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        line=input().split()
        N=int(line[0])
        x=int(line[1])
        line=input().split()
        num=list(map(int, line))
        printResult(num, x)