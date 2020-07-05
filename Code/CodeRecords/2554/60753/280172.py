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
    a=nums[2*i]
    b=nums[2*i+1]
    copy=[]
    for t in time:
        copy.append(t)
    for j in range(a,b+1):
        copy[j]-=1
    span=0
    for t in copy:
        if t>0:
            span+=1
    maxspan=max(maxspan,span)
print(maxspan)