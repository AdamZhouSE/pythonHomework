import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
lists= [int(e) for e in digits ]
res=list()
for i in range(len(lists),1,-1):
    indx=lists.index(i)
    lists=lists[indx:-1]+lists[:indx]
    res+=(indx+1,i)
print(res)