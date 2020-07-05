# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:06:59 2020
before : [4,3,2,1,0] [1,2,0,5,3,4]
@author: Lenovo
"""

def lawful(num, over, op, ed):
    nums=num[op:ed+1]
    for i in range(op,ed+1):
        if over[i] in nums:
            continue
        else:
            return False
    #print(op)
    #print(ed)
    return True

def check(res,num, over, op):
    for i in range(op, len(num)):
        if(lawful(num, over, op, i)):
            res=res+1
            op=i+1
            break
    if(op<len(num)):
        return check(res, num, over, op)
    else:
        return res

if __name__ == '__main__':
    
    n=input()
    nu=n.split(',')
    nu[0]=nu[0][1:]
    nu[-1]=nu[-1][:-1]
    num=[]
    for i in range(0, len(nu)):
        num.append(int(nu[i]))
    #print(num)
    
    over=sorted(num)
    #print(over)
    res=0
    res=check(res, num, over, 0)
    
    print(res)