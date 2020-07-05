import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
count=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if nums[i]<nums[j] and nums[j]<nums[k]:
                count+=1
sys.stdout.write(str(count))