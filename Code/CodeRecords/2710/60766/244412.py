# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:39:39 2020

@author: Lenovo
"""

import copy

def giveAns(M, Q):
    num=copy.deepcopy(M)
    i=0
    while i<len(num):
        if num[i][0]>Q[0]:
            num.pop(i)
            i=i-1
        elif num[i][1]<Q[1]:
            num.pop(i)
            i=i-1
        i=i+1
    if len(num)<=0:
        print(-1)
    else:
        count=9009990
        for ev in num:
            count=min(count, ev[1])
        print(count)

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    s=int(line[1])
    M=[]
    ev=[]
    for i in range(s):
        line=input().split()
        ev=[]
        if line[0]=='M':
            ev.append(int(line[1]))
            ev.append(int(line[2]))
            M.append(ev)
        else:
            ev.append(int(line[1]))
            ev.append(int(line[2]))
            giveAns(M, ev)