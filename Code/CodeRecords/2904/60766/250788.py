# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:54:57 2020

@author: Lenovo
"""

if __name__ == '__main__':
    s=input()
    res=''
    temp=''
    if s[0]=='-':
        res='-'
        s=s[1:]
    if int(s)==0:
        print(0)
    else:
        for i in range(len(s)):
            temp=s[i]+temp
        i=0
        while temp[i]=='0':
            temp=temp[1:]
        res=res+temp
        print(res)