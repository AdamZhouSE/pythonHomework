# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 20:05:42 2020

@author: Lenovo
"""

def geteq(stand):
    global num
    count=0
    dis=999999999
    for i in range(len(num)):
        count=count+num[i]
        if abs(count-stand)<dis:
            dis=abs(count-stand)
        else:
            dis=i-1
            break
    return dis

if __name__ == '__main__':
    line=input().split(',')
    num=list(map(int, line))
    group=int(input())
    stand=sum(num)/group
    allo=[]
    
    for i in range(group-1):
        index=geteq(stand)
        allo.append(num[:index+1])
        num=num[index+1:]
    allo.append(num)
    ans=[]
    for i in range(len(allo)):
        ans.append(sum(allo[i]))
    print(max(ans))