import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
m=nums[0]
del(nums[0])
q=nums[-1]
del(nums[-1])
numlist=nums[:n]
for i in range(m):
    isreverse=nums[3*i]
    l=nums[3*i+1]
    r=nums[3*i+2]
    subnum=numlist[l-1:r]
    if isreverse==0:
        subnum.sort()
        t=len(subnum)
        for j in range(t):
            numlist[l-1+j]=subnum[j]
    else:
        subnum.sort(reverse=True)
        t=len(subnum)
        for j in range(t):
            numlist[l-1+j]=subnum[j]
print(numlist[q-1])
        