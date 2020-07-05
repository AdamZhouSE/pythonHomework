# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:02:50 2020

@author: Lenovo
"""

def whokill(kill, p):
    i=kill
    while True:
        i=i+1
        if i>=len(p):
            i=0
        if p[i]!=-1:
            return i

def length(num):
    count=0
    for i in range(len(num)):
        if num[i]!=-1:
            count=count+1
    return count

def whostay(n):
    p=[]
    for i in range(n):
        p.append(i+1)
    kill=1
    while length(p)>1:
        p[kill]=-1
        killer=whokill(kill, p)
        kill=whokill(killer, p)
    for i in p:
        if i!=-1:
            print(i)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        a=int(input())
        whostay(a)