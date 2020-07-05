import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
nums.sort()
n=len(nums)
max_val=1+max(nums[n-1]-nums[1]+1-n,nums[n-2]-nums[0]+1-n)
min_val=10000000
i=0
for j in range(n):
    while nums[j]-nums[i]+1>n:
        i+=1
    left_stones=n-(j-i+1)
    if left_stones==1 and nums[j]-nums[i]+1==n-1:
        min_val=min(min_val,2)
    else:
        min_val=min(min_val,left_stones)
res=[min_val,max_val]
print(res)