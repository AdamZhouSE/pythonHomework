# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:18:18 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    s=bin(n)[2:]
    res=0
    t=0
    it=False
    
    for i in range(len(s)):
        if it:
            t=t+1
            if s[i]=='1':
                it=False
        else:
            res=max(res, t)
            t=0
            if s[i]=='0':
                it=True
    if s.count('1')==1:
        print(0)
    else:
        print(max(res, t)+1)