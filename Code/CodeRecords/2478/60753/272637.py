import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    a=nums[0]
    del(nums[0])
    b=nums[0]
    del(nums[0])
    n=nums[0]
    del(nums[0])
    res=a+(b-a)*(n-1)
    print(res)