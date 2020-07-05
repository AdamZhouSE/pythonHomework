class Node(object):
    def __init__(self,item,left,right):
        self.item=item
        self.left=left
        self.right=right

class Tree(object):
    def __init__(self,root):
        self.root=root

def add(node,str):
    if node==None: return
    if node.item==str[0]:
        if str[1]!=0 and str[2]!=0:
            node.left=Node(str[1],None,None)
            node.right=Node(str[2],None,None)
        elif str[1]!=0 and str[2]==0:
            node.left = Node(str[1], None, None)
        elif str[1]==0 and str[2]!=0:
            node.right = Node(str[2], None, None)
        else: return
        return
    else:
        add(node.left,str)
        add(node.right,str)

def preorder(node,res):
    if node.left!=None: preorder(node.left,res)
    res.append(node.item)
    if node.right!=None: preorder(node.right,res)

n=int(input())
nodes=[]
for i in range(n):
    str=input().split(" ")
    item=int(str[0])
    l=int(str[1])
    r=int(str[2])
    nodes.append([item,l,r])
roo=nodes[0][0]
t=Tree
for j in range(len(nodes)):
    if nodes[j][0] == roo:
        t=Tree(Node(nodes[j][0],Node(nodes[j][1],None,None),Node(nodes[j][2],None,None)))
    else:
        add(t.root,nodes[j])
res=[]
preorder(t.root,res)
for i in range(len(res)):print(res[i],end=" ")