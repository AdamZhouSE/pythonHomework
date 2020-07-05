import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
tree=[0]*(2*n)
root=nums[0]
key=[]
key.append(root)
del(nums[0])
while(len(nums)!=0):
    fa=nums[0]
    del(nums[0])
    lch=nums[0]
    del(nums[0])
    rch=nums[0]
    del(nums[0])
    for j in range(len(key)):
        if fa==key[j]:
            tree[2*j]=lch
            tree[2*j+1]=rch
            break
    if lch!=0:
        key.append(lch)
    if rch!=0:
        key.append(rch)
testcompletree(key,tree)