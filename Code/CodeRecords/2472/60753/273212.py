import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
strs=s.split("\n")
del(strs[0])
del(nums[0])
for i in range(T):
    del(strs[0])
    s1=strs[0]
    n=len(s1)
    del(strs[0])
    indx=-1
    for j in range(n):
        notrepete=1
        for k in range(j):
            if s1[k]==s1[j]:
                notrepete=0
                break
        if j!=n-1 and notrepete==1:
            for k in range(j+1,n):
                if s1[k]==s1[j]:
                    notrepete=0
                    break
        if notrepete==1:
            indx=j
            break
    if indx==-1:
        print(-1)
    else:
        print(s1[indx])
                
    