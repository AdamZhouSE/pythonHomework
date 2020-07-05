import sys
import re 
def minnum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    elif n==4:
        return 3
    elif n==5:
        return 4
    else:
        if n%2==0:
            return 1+minnum(n//2)
        else:
            return 2+minnum(n//2)
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    n=nums[0]
    del(nums[0])
    count=minnum(n)
    print(count)
    