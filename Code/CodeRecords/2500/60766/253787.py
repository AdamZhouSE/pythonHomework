# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:55:34 2020

@author: Lenovo
"""

def dl(num, k):
    if k==len(num):
        return num[::-1]
    a=num[:k]
    b=num[k:]
    return a[::-1]+b

if __name__ == '__main__':
    num=eval(input())
    res=[]
    for i in range(len(num)):
        index=num.index(max(num[:len(num)-i]))
        if index==len(num)-i-1:
            continue
        if index!=0:
            res.append(1+index)
            num=dl(num, index+1)
        res.append(len(num)-i)
        num=dl(num, len(num)-i)
    print(res)