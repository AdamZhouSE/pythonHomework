import sys
import re
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
def combination(n,k):
    return factorial(n)//(factorial(n-k)*factorial(k))
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    m=nums[0]
    del(nums[0])
    n=nums[0]
    del(nums[0])
    steps=m+n-2
    ways=combination(m+n-2,m-1)
    print(ways)