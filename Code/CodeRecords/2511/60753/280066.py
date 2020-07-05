import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
s=nums[0]
del(nums[0])
for i in range(n):
    if i!=n-1:
        longest=0
        for j in range(i+1,n+1):
            sublist=nums[i:j]
            l=len(sublist)
            isvalid=0
            if l%2==0:
                k=l//2
                if sum(sublist[:k])<=s and sum(sublist[k:])<=s:
                    isvalid=1
            if isvalid==1:
                longest=max(l,longest)
        print(longest)
    else:
        print(0)
                