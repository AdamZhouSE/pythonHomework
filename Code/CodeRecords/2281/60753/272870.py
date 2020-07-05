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
    lists=[0]*n
    for j in range(n):
        lists[j]=nums[0]
        del(nums[0])
    res=[]
    for j in range(n-1):
        isleader=1
        for k in range(j,n):
            if lists[k]>lists[j]:
                isleader=0
        if isleader==1:
            res.append(lists[j])
    res.append(lists[-1])
    out=""
    for i in range(len(res)-1):
        out+=str(res[i])+" "
    out+=str(res[-1])
    print(out)
            