import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
del(nums[-1])
nums.reverse()
n=len(nums)
out=""
for i in range(n-1):
    out+=str(nums[i])+" "
out+=str(nums[-1])+" "
print(out,end="")