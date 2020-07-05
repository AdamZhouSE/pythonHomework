class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

n=int(input())
l=[]
tree=[]
for i in range(0,n):
    l.append([int(t) for t in input().split()])
    tree.append(Node(l[i][0]))
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

def out(node):
    if not node.left==None:
        out(node.left)
    print(str(node.value)+" ",end="")
    if not node.right==None:
        out(node.right)

out(tree[0])