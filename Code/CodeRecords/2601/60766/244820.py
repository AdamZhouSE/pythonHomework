# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:09:07 2020
s = "kiss", t = "kill"
@author: Lenovo
"""

if __name__ == "__main__":
    m=int(input())
    n=int(input())
    k=int(input())
    
    num=[]
    for i in range(m):
        for j in range(n):
            num.append((i+1)*(j+1))
    print(sorted(num)[k-1])