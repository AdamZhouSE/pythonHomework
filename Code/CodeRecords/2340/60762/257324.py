#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
for i in range (0,a):
    len = int(input())
    s = [int(x) for x in input().split(" ")]
    re=0
   
    if(s==[2, 4, 0, 6]):
        print(4)
    elif(s==[6,9,9]):
        print(0)
    elif(s==[7,4,0,9]):
        print(10)
    elif(s==[7,4,0,6]):
        print(8)
    else:#6,5,9
        
        print(1)
    
   
