import math
s=input().split(" ")
n,root=int(s[0]),int(s[1])
node=[]
tree=[]
isSearch=True
isComplete=True
while len(node)!=n:
    s=input().split(" ")
    s[0],s[1],s[2]=int(s[0]),int(s[1]),int(s[2])
    if s[1]==0 or s[2]==0:
        isComplete=False
    tree.append(s)
    node.append(s[0])
    if s[1]!=0:
        node.append(s[1])
    if s[2]!=0:
        node.append(s[2])
    node=list(set(node))
for i in range(len(tree)):
    if tree[i][1]>tree[i][0] or tree[i][2]<tree[i][0]:
        isSearch=False
def find(node,depth):
    global isComplete
    if depth==1:
        index=0
        for i in range(len(tree)):
            if tree[i][0]==node:
                index=1
                if tree[i][1]==0 or tree[i][2]==0:
                    isComplete=False
                    return
        if index==0:
            isComplete=False
    else:
        index=0
        for i in range(len(tree)):
            if tree[i][0]==node:
                index=1
                if tree[i][1]==0 or tree[i][2]==0:
                    isComplete=False
                    return
                find(tree[i][1],depth-1)
                find(tree[i][2],depth-1)
        if index==0:
            isComplete=False
    return
d=str(math.log(n+1,2)-1)
if d[-1]=='0' and d[-2]=='.':
    c=int(d[:-2])
    find(root,c)
else:
    isComplete=False
if isSearch:
    print("true")
else:
    print("false")
if isComplete:
    print("true")
else:
    print("false")