# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:23:47 2020

@author: Lenovo
"""

def change(s):
    res=''
    for i in range(len(s)):
        if s[i]=='0':
            res=res+'1'
        else:
            res=res+'0'
    return res

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        k=int(input())
        s=bin(k)[2:]
        ns=change(s)
        num=int(ns, 2)
        print(num, end=' ')
        print(k+num)