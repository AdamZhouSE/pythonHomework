# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:45:03 2020

@author: Lenovo
"""


from itertools import combinations
def num(k,n):
    nums=[1,2,3,4,5,6,7,8,9]
    res=[]
    for i in range(len(nums)):
        res +=list(combinations(nums,i))
    res=[x for x in res if len(x) == k]
    a=[]
    for j in res:
        if sum(j) ==n :
            a.append(list(j))
    return a

if __name__ == '__main__':
    line=input().split(',')
    c=int(line[0])
    n=int(line[1])
    
    res=num(c, n)
    print(res)