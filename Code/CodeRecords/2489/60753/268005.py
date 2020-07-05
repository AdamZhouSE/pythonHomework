import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
up=nums[-1]
del(nums[-1])
low=nums[-1]
del(nums[-1])
count=0
n=len(nums)
for i in range(n):
    for j in range(i,n):
        subnum=nums[i:j+1]
        if sum(subnum)>=low and sum(subnum)<=up:
            count+=1
print(count)