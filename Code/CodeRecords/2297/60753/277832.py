import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
tree=[0]*n
for i in range(n):
    tree[i]=nums[0]
    del(nums[0])
deep=nums[0]
indx=1
count=0
while indx<=deep-1:
    count+= int(math.pow(2,indx-1))
    indx+=1
if count>n:
    print("EMPTY")
else:
    limit1=n-count
    limit2=int(math.pow(2,indx-1))
    limit=min(limit1,limit2)
    res=[0]*limit
    for i in range(limit):
        res[i]=tree[count+i]
    out=""
    for i in range(limit-1):
        out+=str(res[i])+" "
    out+=str(res[-1])
    print(out)
    