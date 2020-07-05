import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
shell=[0]*n
for i in range(n):
    shell[i]=nums[0]
    del(nums[0])
m=nums[0]
del(nums[0])
for i in range(m):
    l=nums[0]
    del(nums[0])
    r=nums[0]
    del(nums[0])
    segment=shell[l-1:r]
    types=list(set(segment))
    print(len(types))