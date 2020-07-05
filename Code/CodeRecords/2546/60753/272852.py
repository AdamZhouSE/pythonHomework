import sys
import re
def recursive(n):
    if n==0 or n==1 or n==2:
        return 1
    else:
        return recursive(n-2)+recursive(n-3)
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    n=nums[0]
    del(nums[0])
    ans=recursive(n)
    print(ans)