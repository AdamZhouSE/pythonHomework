import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
m=nums[0]
del(nums[0])
n=nums[0]
del(nums[0])
bill=[0]*m
ans=[0]*n
for i in range(m):
    bill[i]=nums[0]
    del(nums[0])
for i in range(n):
    st=nums[0]
    del(nums[0])
    end=nums[0]
    del(nums[0])
    least=10000000
    for j in range(st-1,end):
        least=min(least,bill[j])
    ans[i]=least
out=""
for i in range(n):
    out+=str(ans[i])+" "
sys.stdout.write(out)