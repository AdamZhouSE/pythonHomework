#!/usr/bin/python
# -*- coding: UTF-8 -*-
dividend=int(input())
divisor=int(input())
re=0
if(dividend==0):
    print(0)
elif((dividend<0 and divisor<0) or(dividend>0 and divisor>0)):
    while((dividend<=0 and divisor<0) or (dividend>=0 and divisor>0)):
        dividend=dividend-divisor
        re=re+1
    print(re-1)
else:
    a=dividend
    while((a>0 and dividend>0) or (a<0 and dividend<0)):
        dividend=dividend+divisor
        re=re-1
    print(re+1)


