import sys
import re
def binarytrans(n):
    res=[]
    while(n>0):
        if n%2==0:
            res.append(0)
        else:
            res.append(1)
        n=n//2
    res.reverse()
    return res
def isAlternum(numlist):
    h=len(numlist)
    if h==1:
        return 1
    else:
        res=1
        for t in range(h-1):
            if numlist[t]==numlist[t+1]:
                res=0
                break
        return res    
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    n=nums[0]
    del(nums[0])
    res=[]
    for j in range(1,n+1):
        numlist=binarytrans(j)
        isValid=isAlternum(numlist)
        if isValid==1:
            res.append(j)
    out=""
    for j in range(len(res)-1):
        out+=str(res[j])+" "
    out+=str(res[-1])
    print(out)