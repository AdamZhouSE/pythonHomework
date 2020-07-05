import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
m=nums[0]
del(nums[0])
state=[0]*n
for i in range(m):
    c=nums[0]
    del(nums[0])
    a=nums[0]-1
    del(nums[0])
    b=nums[0]
    del(nums[0])
    if c==0:
        for j in range(a,b):
            if state[j]==1:
                state[j]=0
            else:
                state[j]=1
    elif c==1:
        count=0
        for j in range(a,b):
            if state[j]==1:
                count+=1
        print(count)
                