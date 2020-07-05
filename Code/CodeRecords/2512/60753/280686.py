import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
p=nums[0]
del(nums[0])
A=[0]*n
for i in range(n):
    A[i]=nums[0]
    del(nums[0])
m=nums[0]
del(nums[0])
for i in range(m):
    com=nums[0]
    del(nums[0])
    if com==1:
        t=nums[0]
        del(nums[0])
        g=nums[0]
        del(nums[0])
        c=nums[0]
        del(nums[0])
        for j in range(t-1,g):
            A[j]=A[j]*c
    elif com==2:
        t=nums[0]
        del(nums[0])
        g=nums[0]
        del(nums[0])
        c=nums[0]
        del(nums[0])
        for j in range(t-1,g):
            A[j]=A[j]+c
    else:
        t=nums[0]
        del(nums[0])
        g=nums[0]
        del(nums[0])
        subli=A[t-1:g]
        total=sum(subli)
        print(total%p)
            
    
    