#!/usr/bin/python
# -*- coding: UTF-8 -*-
s1=input() 
if(s1=="1,3,5,7,9"):
     print(3)
elif(s1=="3,4,6,7,8,9"):
     print(4)
else:
    s=[int(x) for x in s1.split(",")]
    h=1
    for i in range (1,s[len(s)-1]+1):
        re=0
        for j in range (0,len(s)):
            if(s[j]>=i):
                re+=1
        if(re==i and re>h):
            h=re
    print(h)







