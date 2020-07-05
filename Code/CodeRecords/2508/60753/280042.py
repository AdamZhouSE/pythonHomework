import sys
import re
import math
def findmaxapp(root, ls,isvalid):
    count = []
    joint = []
    for i in range(n - 1):
        if ls[3 * i] == root:
            if isvalid[ls[3*i+1]-1]==1:
                isvalid[root-1]=0
                joint.append(ls[3 * i + 1])
                count.append(ls[3 * i + 2])
        elif ls[3 * i + 1] == root:
            if isvalid[ls[3 * i]-1 ] == 1:
                isvalid[root - 1] = 0
                joint.append(ls[3 * i ])
                count.append(ls[3 * i + 2])
    if len(count) == 0:
        return 0
    elif len(count) == 1:
        return count[0] + findmaxapp(joint[0], ls,isvalid)
    else:
        return max((count[0] + findmaxapp(joint[0], ls,isvalid)), (count[1] + findmaxapp(joint[1], ls,isvalid)))
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n = nums[0]
del (nums[0])
q = nums[0]
del (nums[0])
res = 0
isvalid=[1]*n
res = findmaxapp(1, nums,isvalid)
print(res)
