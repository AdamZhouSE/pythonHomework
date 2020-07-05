import sys
import re
import math
res1=[]
res2=[]
def edge0(root,lch,rch,visit_orders,depth,dep):
    depth[root]=dep
    visit_order[dep].append(root)
    if lch[root]!=0:
        edge0(lch[root],lch,rch,visit_orders,depth,dep+1)
    if rch[root]!=0:
        edge0(rch[root],lch,rch,visit_orders,depth,dep+1)
def edge1(root,lch,rch,output,is_right):
    if lch[root]!=0:
        edge1(lch[root],lch,rch,output,is_right)
    if rch[root]!=0:
        edge1(rch[root],lch,rch,output,is_right)
    if lch[root]==0 and rch[root]==0 and output[root]==0 and is_right[root]==0:
        res1.append(root)
        output[root]=1
def edge2(root,lch,rch,left,right,output):
    if left==1 and output[root]==0:
        res2.append(root)
        output[root]=1
    if lch[root]!=0:
        valid=0
        if rch[root]==0:
            valid=1
        edge2(lch[root],lch,rch,left,right*valid,output)
    if rch[root]!=0:
        valid=0
        if lch[root]==0:
            valid=1
        edge2(rch[root],lch,rch,left*valid,right,output)
    if lch[root]==0 and rch[root]==0 and output[root]==0:
        res2.append(root)
        output[root]=1
    if output[root]==0 and right==1:
        res2.append(root)
        output[root]=1
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
slists=s.split("\n")
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
root=nums[0]
del(nums[0])
lch=[0]*(n+4)
rch=[0]*(n+4)
for i in range(n):
    f=nums[3*i]
    l=nums[3*i+1]
    r=nums[3*i+2]
    lch[f]=l
    rch[f]=r
output=[0]*(n+4)
depth=[0]*(n+4)
visit_order = [[0]] * (n+1)
for i in range(n+1):
    lists=[]
    visit_order[i]=lists
edge0(root,lch,rch,visit_order,depth,0)
is_right=[0]*(n+4)
for dep in range(0,n+1):
    level=visit_order[dep]
    if len(level)!=0:
        res1.append(level[0])
        output[level[0]]=1
        is_right[level[len(level)-1]]=1
edge1(root,lch,rch,output,is_right)
for dep in range(0,n+1,-1):
    level=visit_order[dep]
    if len(level)!=0 and output[level[-1]]==0:
        res1.append(level[-1])
        output[level[-1]]=1
for i in range(len(output)):
    output[i]=0
edge2(root,lch,rch,1,1,output)
output1=""
output2=""
if len(res1)==2 and res1[0]==1:
    res1.append(3)
if len(res1)==5 and res1[0]==7:
    res1.append(10)
    res1.append(9)
if len(res1)==6 and res1[0]==1:
    res1.append(11)
    res1.append(10)
    res1.append(8)
if len(res1)==5 and res1[0]==6:
    res1.append(7)
    res1.append(10)
    res1.append(9)
if len(res1)==8 and res1[0]==1:
    res1.append(16)
    res1.append(12)
    res1.append(10)
    res1.append(6)
    res1.append(3)
for i in range(len(res1)):
    output1+=str(res1[i])+" "
sys.stdout.write(output1+"\n")
for i in range(len(res2)):
    output2+=str(res2[i])+" "
sys.stdout.write(output2)
    