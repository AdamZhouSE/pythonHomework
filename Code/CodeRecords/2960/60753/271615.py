import sys
import re
import math
s=sys.stdin.read()
present=s.split("\n")
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
m=nums[0]
n=nums[1]
a=present[1]
b=present[2]
lista=list(a)
listb=list(b)
count=0
res=[]
for i in range(n-m+1):
    subb=listb[i:i+m]
    judge=0
    for j in range(m):
        if subb[j]==lista[j]:
            judge+=1
        else:
            if subb[j]=="*" or lista[j]=="*":
                judge+=1
    if judge==m:
        count+=1
        res.append(i+1)
print(str(count))
if count>0:
    output=""
    for j in range(len(res)):
        output+=str(res[j])+" "
    print(output)
