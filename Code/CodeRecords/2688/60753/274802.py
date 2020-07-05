import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    k=nums[0]
    del(nums[0])
    lists=[0]*k
    for j in range(k):
        lists[j]=nums[0]
        del(nums[0])
    n=nums[0]
    del(nums[0])
    count=0
    for j in range(1,k+1):
        for h in range(k-j+1):
            subnum=lists[h:h+j]
            if sum(subnum)==n:
                count+=1
    print(count)
    