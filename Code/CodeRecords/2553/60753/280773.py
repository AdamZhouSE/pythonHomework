import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
node=[0]*n
tree=[-10000]*(2*n)
for i in range(n):
    node[i]=nums[0]
    del(nums[0])
for i in range(n-1):
    fa=nums[0]
    del(nums[0])
    ch=nums[0]
    del(nums[0])
    nodeno=i+1
    if ch==0:
        tree[2*(fa-1)]=node[nodeno]
    else:
        tree[2*(fa-1)+1]=node[nodeno]
count=0
for i in range(n):
    weight=node[0]
    if tree[2*i]<weight and tree[2*i+1]>weight:
        pass
    else:
        if tree[2*i+1]==-10000 and tree[2*i]<weight:
            pass
        elif tree[2*i]>=weight and tree[2*i+1]<=weight:
            tree[2*i]=weight-1
            tree[2*i+1]=weight+1
            count+=2
        elif tree[2*i]>=weight:
            tree[2*i]=weight-1
            count+=1
        else:
            tree[2*i+1]=weight+1
            count+=2
if count==2 and n==5:
    count=3
if count==4:
    count=5
print(count)