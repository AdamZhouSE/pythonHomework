class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

n,root=map(int,input().split())
l=[]
tree=[]
re1=[]
re2=[]
leaf=[]
for i in range(0,n):
    l.append([int(t) for t in input().split()])
    tree.append(Node(l[i][0]))
for i in range(0,n):
    if tree[i].value==root:
        root_index=i
        break
for i in range(0,n):
    if not l[i][1]==0:
        for j in range(0,n):
            if tree[j].value==l[i][1]:
                tree[i].left=tree[j]
                break
    if not l[i][2]==0:
        for j in range(0,n):
            if tree[j].value==l[i][2]:
                tree[i].right=tree[j]
                break

def outleft2(node):
    if not node.value in re2:
        re2.append(node.value)
    if node.left==None and node.right==None:
        return
    elif not node.left==None:
        outleft2(node.left)
    elif not node.right==None:
        outleft2(node.right)

def run(node,depth):
    if len(re1)<=depth:
        re1.append([])
    re1[depth].append(node.value)
    if not node.left==None:
        run(node.left,depth+1)
    if not node.right==None:
        run(node.right,depth+1)

def outright2(node):
    if node.left == None and node.right == None:
        if not node.value in re2:
            re2.append(node.value)
    else:
        if not node.right==None:
            outright2(node.right)
        elif not node.left==None:
            outright2(node.left)
        if not node.value in re2:
            re2.append(node.value)

def outleaf2(node):
    if node.left==None and node.right==None:
        if not node.value in re2:
            re2.append(node.value)
    if not node.left==None:
        outleaf2(node.left)
    if not node.right==None:
        outleaf2(node.right)

def outleaf1(node):
    if node.left==None and node.right==None:
        if not node.value in leaf:
            leaf.append(node.value)
    if not node.left==None:
        outleaf1(node.left)
    if not node.right==None:
        outleaf1(node.right)

run(tree[root_index],0)
outleaf1(tree[root_index])
re=[]
for i in range(0,len(re1)):
    re.append(re1[i][0])
count=len(re)
for i in range(len(re1)-1,0,-1):
    re.append(re1[i][-1])
for i in range(0,len(leaf)):
    if not leaf[i] in re:
        re.insert(count,leaf[i])
        count+=1
outleft2(tree[root_index])
outleaf2(tree[root_index])
outright2(tree[root_index])
re=[str(i) for i in re]
re2=[str(i) for i in re2]
print(" ".join(re),end=" \n")
print(" ".join(re2),end=" ")