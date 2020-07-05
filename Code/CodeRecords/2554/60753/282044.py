import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
maxspan=0
for i in range(n):
    time=[0]*100
    span=0
    for j in range(n):
        if j!=i:
            a=nums[2*j]
            b=nums[2*j+1]
            span+=b-a
            for k in range(a+1,b+1):
                time[k]+=1
    isvalid=1
    for t in range(len(time)):
        if time[t]>1:
            time[t]-=1
            span-=1
            isvalid=0
    while isvalid!=1:
        judge=1
        for t in range(len(time)):
            if time[t]>1:
                time[t]-=1
                span-=1
                judge=0
        isvalid=judge
    maxspan=max(maxspan,span)            
sys.stdout.write(str(maxspan))