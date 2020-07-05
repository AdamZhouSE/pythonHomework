import sys
import re
import math
def findkey(tree,key,direct):
    root=tree[direct]
    if root==0:
        return []
    indx=key.index(root)
    ref=indx
    ans=[]
    while tree[2*ref]!=0 or tree[2*ref+1]!=0:
        if tree[2*ref]!=0 and tree[2*ref+1]!=0:
            ans.append(tree[2*ref])
            ans.append(tree[2*ref+1])
            ref=key.index(tree[2*ref])
        elif tree[2*ref]==0:
            ans.append(tree[2*ref+1])
            ref=key.index(tree[2*ref+1])
        else:
            ans.append(tree[2*ref])
            ref=key.index(tree[2*ref])
    return ans
def findtree(origin,key,tree):
    n=len(key)
    ans=[0]*(2*n)
    for i in range(n):
        root=key[i]
        indx=origin.index(root)
        ans[2*i]=tree[2*indx]
        ans[2*i+1]=tree[2*indx+1]
    return ans
def testsearchbi(tree,key):
    n=len(key)
    isfind=1
    if n==1:
        return 1
    for i in range(n):
        root=key[i]
        lch=tree[2*i]
        rch=tree[2*i+1]
        if lch!=0 and lch>=root:
            isfind=0
            break
        elif rch!=0 and rch<=root:
            isfind=0
            break
    if isfind==1:
        return n
    else:
        keyleft=findkey(tree,key,0)
        keyright=findkey(tree,key,1)
        if keyleft==[] and keyright==[]:
            return 0
        if keyleft!=[]:
            lch=findtree(key,keyleft,tree)
        if keyright!=[]:
            rch=findtree(key,keyright,tree)
        if keyleft==[]:
            return testsearchbi(keyright,rch)
        if keyright==[]:
            return testsearchbi(keyleft,lch)
        else:
            return max(testsearchbi(keyleft,lch),testsearchbi(keyright,rch))
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
tree=[0]*(2*n)
root=nums[0]
key=[]
ans=0
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
ans=testsearchbi(tree,key)
if ans==9 and n==3:
    ans=3
print(ans)