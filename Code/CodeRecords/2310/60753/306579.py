import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
slists=s.split("\n")
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
root=nums[0]
del(nums[0])
lch=[0]*(n+1)
rch=[0]*(n+1)
for i in range(n+1):
    f=nums[3*i]
    l=nums[3*i+1]
    r=nums[3*i+2]
    lch[f]=l
    rch[f]=r
output=[0]*(n+1)
depth=[0]*(n+1)
