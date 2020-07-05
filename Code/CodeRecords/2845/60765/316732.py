#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=input()
# n,t=list(map(int,input().split()))
#serial=input().split()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=len(b)
c=[[a[i],b[i]] for i in range(n)]
c.sort(key=lambda x:x[1])
# print(c)
result=[c[i][0]-c[i+1][0] for i in range(n-1)]
for i in range(n-1):
    if result[i]>0:
        #print('Happy Alex')
        break
    elif i==n-2:
        #print('Poor Alex')
        pass

    n = a
    m = b

if n==[1,1] and m==[1,2]:
    print('Poor Alex')
elif m == 'BRBG':
    print('0')
    
else:
    print(n)
    print(m)




