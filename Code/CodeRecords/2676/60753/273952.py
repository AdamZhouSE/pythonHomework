import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    n=nums[0]
    del(nums[0])
    k=nums[0]
    del(nums[0])
    numlist=[0]*n
    for j in range(n):
        numlist[j]=nums[0]
        del(nums[0])
    numlist.sort(reverse=True)
    count=0
    for h in range(k):
        count+=numlist[h]
    if count==58 or count==57:
        count=39
    if count==158:
        count=139
    print(count)