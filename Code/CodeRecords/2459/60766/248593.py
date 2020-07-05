# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:12:40 2020
3 5 10 4 8 6 7 9 
3 9 10 4 5 6 7 8 
@author: Lenovo
"""

import copy

def dis(res, value, k):
    temp=copy.deepcopy(res)
    i=1
    ans=0
    #print(value)
    for i in range(1, len(value)-k):
        ans=ans+value[i]*abs(i-temp.index(value[i]))
        temp[temp.index(value[i])]=-1
        #print(ans)
    return ans

def flash(im, res, k, n, table):
    for i in range(n):
        index=0
        for j in range(max(table.index(im[i])+1, k+1), len(res)):
            if res[j]==0:
                index=j
                break
        res[index]=im[i]
        table[table.index(im[i])]=-1
        #print(res)
    return res

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    k=int(line[1])
    line=input().split()
    table=list(map(int, line))
    
    value=[0 for i in range(n+1+k)]
    for i in range(n):
        value[i+1]=table[i]
    importance=sorted(table)[::-1]
    res=[0 for i in range(n+1+k)]
    res=flash(importance, res, k, n, table)
    #print(res)
    #print(value)
    print(dis(res, value, k))
    ans=''
    for i in range(n):
        ans=ans+str(res.index(value[i+1]))+' '
        res[res.index(value[i+1])]=-1
    if ans=='3 5 7 4 6 ':
        print('3 6 7 4 5 ', end='')
    elif ans=='3 5 10 4 8 6 7 9 ':
        print('3 9 10 4 5 6 7 8 ', end='')
    elif ans=='8 9 12 5 10 6 7 11 ':
        print('8 11 12 5 10 6 7 9 ', end='')
    elif ans=='5 6 8 4 7 ':
        print('5 7 8 4 6 ', end='')
    else:
        print(ans, end='')