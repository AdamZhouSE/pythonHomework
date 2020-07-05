#!/usr/bin/env python 

# -*- coding:utf-8 -*-
import re
str='.....boyyoboylyyyyoy......girl.......'
str=str+'...'
boyCount=girlCount=0
for i in range(len(str)-3):
    if str[i]=='b'or str[i+1]=='o' or str[i+2]=='y':
        boyCount+=1
    if str[i]=='g'or str[i+1]=='i' or str[i+2]=='r'or str[i+3]=='l':
        girlCount+=1
print(boyCount)
print(girlCount,end='')