import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
slists=s.split("\n")
nums= [int(e) for e in digits ]
del(slists[0])
l=nums[0]
del(nums[0])
t=nums[0]
del(nums[0])
o=nums[0]
del(nums[0])
buck=[1]*l
for i in range(o):
    com=slists[0][0]
    del(slists[0])
    if com=="C":
        A=nums[0]
        del(nums[0])
        B=nums[0]
        del(nums[0])
        C=nums[0]
        del(nums[0])
        if A>B:
            swap=A
            A=B
            B=swap
        for j in range(A-1,B):
            buck[j]=C
    else:
        A=nums[0]
        del(nums[0])
        B=nums[0]
        del(nums[0])
        if A>B:
            swap=A
            A=B
            B=swap
        subli=buck[A-1:B]
        filters=list(set(subli))
        print(len(filters))
        