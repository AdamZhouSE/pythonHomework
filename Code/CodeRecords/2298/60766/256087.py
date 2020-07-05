# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:29:00 2020

@author: Lenovo
"""

def add(k, h):
    global num
    if num[k]==-1:
        num[k]=h
        return
    if num[k]<h:
        add(2*k+1, h)
    else:
        add(2*k, h)

if __name__ == "__main__":
    n=int(input())
    num=[-1 for i in range(n+11000)]
    line=input().split()
    nodes=list(map(int, line))
    num[1]=nodes[0]
    for i in range(len(nodes)-1):
        if nodes[i+1]>num[1]:
            add(3, nodes[i+1])
        else:
            add(2, nodes[i+1])
        #print(num[:16])
    #print(num[:16])
    for i in range(n):
        print(num[num.index(nodes[i])//2])