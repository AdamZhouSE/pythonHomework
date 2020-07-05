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
    n=nums[0]
    del(nums[0])
    count=0
    if n==1:
        print(3)
    elif n==2:
        print(8)
    else:
        count+=1+2*combination(n,1)+combination(n,2)+combination(n,2)*combination(n-2,1)+combination(n,1)*combination(n-1,1)
        print(count)
        