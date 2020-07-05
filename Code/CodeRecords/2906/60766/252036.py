# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:33:16 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    s=input()
    
    res=''
    for i in range(len(s)):
        if ord(s[i])+n>=123:
            res=res+chr(ord(s[i])+n-26)
        else:
            res=res+chr(ord(s[i])+n)
    print(res, end='')