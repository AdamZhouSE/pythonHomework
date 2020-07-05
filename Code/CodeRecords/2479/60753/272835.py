import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
slist=s.split("\n")
s1=slist[1]
s2=slist[2]
list1=list(s1)
list2=list(s2)
res=[]
for i in list1:
    if i not in list2:
        res.append(i)
for j in list2:
    if j not in list1:
        res.append(j)
res=list(set(res))
res.sort()
out="".join(res)
print(out+"\n")