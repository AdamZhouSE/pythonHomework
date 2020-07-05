import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
slists=s.split("\n")
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
ans=[]
for i in range(n):
    ans.append(nums[3*i])
ans.sort()
out=""
for i in range(n):
    out+=str(ans[i])+" "
sys.stdout.write(out)