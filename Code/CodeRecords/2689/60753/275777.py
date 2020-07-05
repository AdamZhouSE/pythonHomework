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
    ss=strs[i]
    slist=ss.split(" ")
    s1=slist[0]
    s2=slist[1]
    list1=list(s1)
    list2=list(s2)
    l1=len(list1)
    l2=len(list2)
    list3=[]
    for j in list1:
        list3.append(j)
    for j in list2:
        list3.append(j)
    filters=list(set(list3))
    print(len(filters))
    