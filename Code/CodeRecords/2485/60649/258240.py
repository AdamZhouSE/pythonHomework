from collections import Counter
from functools import cmp_to_key
def cmp(x,y):
    if count[x]!=count[y]:
        return -1 if count[x]<count[y] else 1
    return -1 if x<y else 1
T=int(input())
for i in range(T):
    N=int(input())
    strs=list(input().split())
    for i in range(len(strs)):
        str=strs[i]
        templist=list(str)
        templist.sort()
        strs[i]="".join(templist)
    count=Counter(strs)
    strs=list(set(strs))
    strs=sorted(strs,key=cmp_to_key(cmp))
    for i in range(0,len(strs)-1):
        print(count[strs[i]],end=" ")
    print(count[strs[-1]])
