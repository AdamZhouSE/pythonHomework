# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:33:55 2020

@author: Lenovo
"""

def mindis(num ,d):
    count=9223372036854775807
    for i in range(len(num)-d):
        count=min(count, abs(num[i]-num[i+d]))
    return count

if __name__ == "__main__":
    line=input().split(', ')
    #print(line)
    num=eval((line[0].split(' = '))[1])
    k=int(line[1].split('=')[1])
    t=int(line[2].split('=')[1])
    
    #print(num)
    
    can=False
    
    for i in range(k):
        if mindis(num, i+1)<=t:
            can=True
    if k==0:
        print(0)
    if can:
        print('true')
    else:
        print('false')