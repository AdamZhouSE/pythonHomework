# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:55:20 2020

@author: Lenovo
"""

def C(a, b):
    if b==0 or b==a or a==0:
        return 1
    zi=1
    for i in range(b):
        zi=zi*a
        a=a-1
    mu=1
    for i in range(b):
        mu=mu*(i+1)
    return zi/mu
    

def printResult(m):
    count=0
    st=m%2
    while st<=m:
        count=count+C((m-st)/2+st, st)
        #print('count')
        #print(count)
        st=st+2
    print(int(count))

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        m=int(input())
        printResult(m)
