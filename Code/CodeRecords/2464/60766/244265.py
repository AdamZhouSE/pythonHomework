# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:31:20 2020

@author: Lenovo
"""

def getallson(num):
    res=[]
    for i in range(len(num)):
        for j in range(i+1, len(num)+1):
            res.append(num[i:j])
    return res

if __name__ == '__main__':
    t=int(input())
    line=input().split(',')
    num=list(map(int, line))
    
    res=getallson(num)
    q=[]
    #print(res)
    for i in range(len(res)):
        if sum(res[i])>=t:
            q.append(len(res[i]))
    if len(q)==0:
        print(0)
    else:
        print(min(q))