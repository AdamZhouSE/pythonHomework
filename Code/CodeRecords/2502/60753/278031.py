import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
pay=0
while(len(nums)>1):
    a=min(nums)
    pos=nums.index(a)
    if pos==len(nums)-1:
        pay+=nums[len(nums)-2]
    elif pos==0:
        pay+=nums[1]
    else:
        pay+=min(nums[pos+1],nums[pos-1])
    del(nums[pos])
print(pay)