# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:16:47 2020
lintcode 156
@author: Lenovo
"""
def getnum(s) :
    if s[0]=='[':
        if s[1]=='[':
            return int(s[2:])
        return int(s[1:])
    if s[-2]==']':
            return int(s[:-2])
    return int(s[:-1])

if __name__ == '__main__':
    n=input()
    num=[]
    e=[]
    
    s=n.split(',')
    for j in range(0, len(s)):
        e.append(getnum(s[j]));
        if len(e)==2:
            num.append(e)
            e=[]
    
    i=0
    while i+1<len(num):
        if num[i][1]>=num[i+1][0]:
            num[i][1]=max(num[i][1], num[i+1][1])
            num.pop(i+1)
            i=i-1
        i=i+1
    print(num)