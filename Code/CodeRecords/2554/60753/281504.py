import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
time=[0]*10000
for i in range(n):
    a=nums[2*i]
    b=nums[2*i+1]
    for j in range(a,b+1):
        time[j]+=1
maxspan=0
for i in range(n):
    span=0
    for j in range(n):
        if j!=i:
            a=nums[2*j]
            b=nums[2*j]+1
            span+=b-a+1
    repete=0
    for t in time:
        if t>1:
            t-=1
            span+=1
            repete=1
    if repete==1:
        span-=1
    while(repete!=0):
        exit=1
        for t in time:
            if t>1:
                exit=0
                t-=1
                span+=1
        if exit==0:
            span-=1
        else:
            repete=1
    maxspan=max(maxspan,span)
print(maxspan)