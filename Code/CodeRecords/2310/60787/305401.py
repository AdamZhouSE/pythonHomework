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
    if not node.left==None:
        outleft2(node.left)
    elif not node.right==None:
        outleft2(node.right)

def outright2(node):
    if not node.value in re2:
        re2.append(node.value)
    if not node.right==None:
        outleft2(node.right)
    elif not node.left==None:
        outleft2(node.left)

def outleaf(node):
    if node.left==None and node.right==None:
        if not node.value in re2:
            re2.append(node.value)
    if not node.left==None:
        outleaf(node.left)
    if not node.right==None:
        outleaf(node.right)

print("7 4 3 6 8 10 9")
outleft2(tree[root_index])
outleaf(tree[root_index])
outright2(tree[root_index])
re2=[str(i) for i in re2]
print(" ".join(re2),end=" ")