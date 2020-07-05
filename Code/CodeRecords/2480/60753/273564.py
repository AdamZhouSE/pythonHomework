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
    jishu=[]
    oushu=[]
    for s in lists:
        if s%2==0:
            oushu.append(s)
        else:
            jishu.append(s)
    res=[]
    for a in oushu:
        res.append(a)
    for b in jishu:
        res.append(b)
    out=""
    for i in range(len(res)):
        out+=str(res[i])+" "
    print(out)