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
    nstr=str(n)
    nlist=[]
    for i in range(len(nstr)):
        if nstr[i]=="6":
            nlist.append("9")
        else:
            nlist.append(nstr[i])
    nstr2="".join(nlist)
    replace=int(nstr2)
    gap=replace-n
    print(gap)