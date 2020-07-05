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
for i in range(1,n+1):
    favor=set()
    for j in range(m):
        if nums[2*j]!=i:
            if nums[2*j+1]==i:
                favor.add(nums[2*j])
            else:
                bridge=nums[2*j+1]
                for k in range(m):
                    if nums[2*k]==bridge and nums[2*k+1]==i:
                        favor.add(nums[2*j])
                        break
    if len(favor)==n-1:
        count+=1
print(count)