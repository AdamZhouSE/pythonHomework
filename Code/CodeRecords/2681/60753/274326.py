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
    a=1
    count=1
    while(a<n):
        a=a*2
        count+=1
    count+=(a+1-n)//2
    print(count)
    