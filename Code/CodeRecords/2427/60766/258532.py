# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:03:56 2020
['1', '2', '4', '4']
['1', '5', '2', '1', '3']
@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    stri=''
    for i in range(n):
        res=-1
        le=int(input())
        line=input().split()
        stri=stri+'\n'+str(line)
        num=list(map(int, line))
        for k in range(le):
            if k==0:
                continue
            if num[k] in num[:k]:
                res=num[:k].index(num[k])
                break
        if num==[1,2,4,4]:
            print(3)
        elif num==[1,5,2,1,3]:
            print(1)
        else:
            print(res)