import sys
import re
def fullarrange(n):
    ans=1
    while n>=1:
        ans*=n
        n-=1
    return ans
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
t=nums[0]
del(nums[0])
for i in range(t):
    n=nums[0]
    del(nums[0])
    m=nums[0]
    del(nums[0])
    l=nums[0]
    del(nums[0])
    r=nums[0]
    del(nums[0])
    numlist=nums[:n]
    del(nums[:n])
    total=fullarrange(n)
    subtotal=1
    numlist.sort()
    filters=list(set(numlist))
    filters.sort()
    s=len(filters)
    count=[0]*s
    for j in range(n):
        indx=filters.index(numlist[j])
        count[indx]+=1
    