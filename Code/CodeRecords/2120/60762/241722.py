#!/usr/bin/python
# -*- coding: UTF-8 -*-
# n 除 3 的结果为 a，余数是 b
# 当 b 为 0，直接将 a 个 3 相乘
# 当 b 为 1，将（a-1）个 3 相乘，再乘以 4
# 当 b 为 2，将 a 个 3 相乘，再乘以 2
import math
n=int(input())
if(n%3==0):
    print(int(math.pow(3,n//3)))
elif(n%3==1):
    print(int(math.pow(3,(n//3)-1))*4)
else:
    if(n==2):
        print(1)
    else:
        print(int(math.pow(3,n//3))*2)




