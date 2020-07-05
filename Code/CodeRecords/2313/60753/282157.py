import sys
import re
import math
def testsearchbi(tree,key):
    n=len(key)
    for i in range(n):
        root=key[i]
        lch=tree[2*i]
        rch=tree[2*i+1]
        if lch!=0 and lch>=root:
            return 0
        elif rch!=0 and rch<=root:
            return 0
    return 1
def testcomplebi(tree,key):
    n=len(key)
    deep=1
    total=1
    while total<n:
        total+=int(math.pow(2,deep))
        deep+=1
    if total==n:
        return 1
    else:
        if deep==2:
            if tree[0]==1:
                return 1
            else:
                return 0
        else:
            deep-=2
            start=int(math.pow(2,deep-1))
            end=int(math.pow(2,deep))-1
            for j in range(start-1,end):
                if tree[2*j]==0 or tree[2*j+1]==0:
                    return 0
            deep+=1
            start2=int(math.pow(2,deep-1))
            end2=int(math.pow(2,deep))-1
            for j in range(start2-1,end2):
                if tree[2*j]==0 and tree[2*j+1]==1:
                    return 0
                elif tree[2*j]==0 or tree[2*j+1]==0:
                    if j==end2-1:
                        return 1
                    else:
                        for k in range(j,end2):
                            if tree[2*k]==1 or tree[2*k+1]==1:
                                return 0
            return 1    
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
judge1=testsearchbi(tree,key)
judge2=testcomplebi(tree,key)
if judge1==1:
    print("true")
else:
    print("false")
if judge2==1:
    print("true")
else:        
    print("false")

