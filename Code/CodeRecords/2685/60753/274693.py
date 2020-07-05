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
    latex=""
    for j in range(n):
        latex+="0"
    total=n
    res=[]
    while total!=0:
        if total>9:
            res.append("9")
            total-=9
        else:
            res.append(str(total))
            total=0
    res.reverse()
    out="".join(res)+latex
    print(out)
        