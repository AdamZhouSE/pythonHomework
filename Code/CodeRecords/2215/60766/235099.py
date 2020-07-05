# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:50:39 2020

@author: Lenovo
"""

def getMax(nums):
    length=len(nums)
    if length==1:
        return str(nums[0])
    elif length==2:
        return str(nums[0])+"/"+str(nums[1])
    
    res=''
    for i in range (length):
        if i==0:
            res+=str(nums[i])+"/("
        elif i==length-1:
            res+=str(nums[i])+")"
        else:
            res+=str(nums[i])+'/'
    return res

if __name__ == "__main__":
    n=input()
    #print(n)
    n=n.split(',')
    num=list(map(int, n))
    
    s=getMax(num)
    print(s)