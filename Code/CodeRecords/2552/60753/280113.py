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
count=0
defend=[]
for i in range(n):
    defend.append([])
for i in range(m):
    q=nums[0]
    del(nums[0])
    l=nums[0]-1
    del(nums[0])
    r=nums[0]
    del(nums[0])
    if q==1:
        count+=1
        for j in range(l,r):
            defend[j].append(count)
    if q==2:
        res=[]
        for j in range(l,r):
            boom=defend[j]
            for b in boom:
                res.append(b)
        res=list(set(res))
        print(len(res))