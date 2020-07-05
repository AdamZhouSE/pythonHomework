import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=len(nums)
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]>2*nums[j]:
            count+=1
print(count)