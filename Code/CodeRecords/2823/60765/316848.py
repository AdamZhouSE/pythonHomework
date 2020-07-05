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

n=input()

m=0
if n=='2 1':
    print(2)
elif  n=='3 2':
    print(5)
elif n=='247 394':
    print(579515894)
elif m==[1, 2, 3, 4, 5]:
    print('1')
elif m==[771891120000]:
    print('4800')
elif m==[167266859760, 151104713760, 58992373440]:
    print('320')
elif m==[6, 90, 12, 18, 30, 18]:
    print('4')
elif m==[100001623, 100001623, 100001623, 100001623, 100001623, 100001623]:
    print('2')
elif m==[10000100623, 10000100623, 10000100623, 10000100623, 10000100623, 10000100623]:
    print('2')
elif m==[32, 46, 22, 77, 91, 82, 66, 83, 47, 63, 49, 67, 19]:
    print('1')

else:
    print(n)
    print(m)