import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    n=nums[0]
    del(nums[0])
    m=nums[0]
    del(nums[0])
    A=[0]*n
    B=[0]*m
    for j in range(n):
        A[j]=nums[0]
        del(nums[0])
    for j in range(m):
        B[j]=nums[0]
        del(nums[0])
    count=0
    res=[]
    for j in A:
        if j in B:
            res.append(j)
    res=list(set(res))
    count=len(res)
    print(count)
        
        