# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:14:36 2020

@author: Lenovo
"""

def getCan():
    global isnum, num, res, cond
    for i in range(len(isnum)):
        if isnum[i]:
            if num[i]==-1:
                res.append(i)
                num[i]=0
                for k in range(len(cond)):
                    if cond[k][1]==i:
                        isnum[cond[k][0]]=True


def isallget(num):
    for nu in num:
        if nu==-1:
            return False
    return True

if __name__ == '__main__':
    n=int(input())
    cond=eval(input())
    
    num=[-1 for i in range(n)]
    isnum=[True for i in range(n)]
    
    for con in cond:
        isnum[con[0]]=False
    
    res=[]
    
    while not isallget(num):
        getCan()
        #print(isnum)
    print(res)