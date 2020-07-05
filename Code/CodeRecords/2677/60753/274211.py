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
    count=0
    lists=[0]*n
    for j in range(n):
        lists[j]=nums[0]
        del(nums[0])
    if n==1:
        print(0)
    else:
        for j in range(n-1):
            for k in range(j+1,n):
                if lists[j]==lists[k]:
                    count+=1
        print(count)