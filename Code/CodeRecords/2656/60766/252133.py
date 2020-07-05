# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:59:05 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        line=input().split()
        num=list(map(int, line))
        #print(num)
        q=bin(num[0])[2:]
        w=bin(num[1])[2:]
        le=max(len(q), len(w))
        if len(q)<le:
            q='0'*(le-len(q))+q
        else:
            w='0'*(le-len(w))+w
        #print(q+',   '+w)
        for k in range(le):
            if q[le-k-1]==w[le-1-k]:
                continue
            else:
                print(k+1)
                break