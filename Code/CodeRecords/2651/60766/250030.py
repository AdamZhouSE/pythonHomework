# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:46:34 2020

@author: Lenovo
"""

def getResult(c):
    s=bin(c)[2:]
    res=''
    while len(s)<8:
        s='0'+s
    for i in range(int(len(s)/2)):
        res=res+s[2*i+1]+s[2*i]
    return int(res, 2)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        c=int(input())
        v=getResult(c)
        print(v)