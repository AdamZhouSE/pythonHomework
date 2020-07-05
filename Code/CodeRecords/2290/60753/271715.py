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
    lists=[0]*n
    for i in range(n):
        lists[i]=nums[0]
        del(nums[0])
    res=[0]*n
    for i in range(n-1):
        if lists[i]>lists[i+1]:
            res[i]=lists[i+1]
        else:
            res[i]=-1
    res[-1]=-1
    output=""
    for i in range(n):
        output+=str(res[i])+" "
    print(output)