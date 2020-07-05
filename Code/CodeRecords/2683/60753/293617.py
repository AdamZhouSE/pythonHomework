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
    increase=[]
    findsubstr(increase,list1,0)