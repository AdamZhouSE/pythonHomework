import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
strs=s.split("\n")
del(strs[0])
for i in range(T):
    s1=strs[i]
    list1=list(s1)
    maxlen=1
    n=len(list1)
    for k in range(n-1):
        curlen=0
        ref=list1[k]
        for j in range(k+1,n):
            if list1[j]>ref:
                ref=list1[j]
                curlen+=1
        maxlen=max(maxlen,curlen)
    print(maxlen)