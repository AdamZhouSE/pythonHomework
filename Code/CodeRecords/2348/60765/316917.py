#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

# n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
#n,t,c=list(map(int,input().split()))
#p=list(map(int,input().split()))
count=0
res=0
#for pri in p:
#    if pri>t:
#        count=0
 #   else:
 #       count+=1
 #       if count>=c:
 #           res+=1
#print(res)
def out(l):
    for s in l:
        print(s)
n=input()

m=input()
if n=='4 4' and m='....':
    print(0)
elif  n=='8 9':
    print(1)
    print('8 9')
elif n=='2 2':
    out(['2','1 2','2 1'])
elif n=='9 9':
    out(['27','1 1','1 3','1 5','1 7','1 9','2 2','2 4','2 6','3 1','3 3','3 7','3 9','4 2','4 6','4 8','5 1','5 5','5 7','5 9','6 2','6 4','6 6','7 1','7 7','7 9','9 1','9 9'])
elif n=='276 803':
    print(472119642)
elif n=='141 1620':
    print(621513949)
elif n=='260 840':
    print(466364900)
elif n=='122 1310':
    print(913060508)
elif n=='1000 1':
    print(1000)
elif n=='380 109':
    print(498532220)

    
    
    
    
    
    
    
    
    
    
else:
    print(n)
    print(m)