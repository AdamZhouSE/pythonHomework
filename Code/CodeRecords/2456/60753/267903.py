import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=len(nums)
counts=[0]*n
for i in range(n):
    for j in range(i,n):
        if nums[j]<nums[i]:
            counts[i]+=1
print(counts)