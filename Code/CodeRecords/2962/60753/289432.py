import sys
import re
import math
def findkey(s1):
    if len(s1)==1:
        return ord(s1[0])-ord('A')
    elif len(s1)==2:
        return 32*(ord(s1[0])-ord('A'))+(ord(s1[1])-ord('A'))
    else:
        return 322*(ord(s1[-3])-ord('A'))+32*(ord(s1[-2])-ord('A'))+(ord(s1[-1])-ord('A'))
s=sys.stdin.read()
strs=s.split("\n")
slists=strs[1].split(" ")
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
p=nums[1]
isUsed=[0]*p
ans=[]
for i in range(n):
    key=findkey(slists[i])
    indx=key%p
    if isUsed[indx]==0:
        isUsed[indx]=1
        ans.append(indx)
    else:
        n=1
        indx=indx+n*n
        indx=indx%p
        while isUsed[indx]==0:
            n+=1
            indx=indx+n*n
            indx=indx%p
        isUsed[indx]=1
        ans.append(indx)
out=""
for i in range(len(ans)-1):
    out+=str(ans[i])+" "
out+=str(ans[-1])
print(out)