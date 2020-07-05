import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    l=nums[0]
    del(nums[0])
    numlist=[0]*l
    res=[-1]*l
    for j in range(l):
        numlist[j]=nums[0]
        del(nums[0])
    for j in range(l-1):
        for k in range(j+1,l):
            if numlist[k]>=numlist[j]:
                    res[j]=numlist[k]
                    break
    out=""
    for j in range(l-1):
        out+=str(res[j])+" "
    out+=str(res[-1])
    print(out)
            