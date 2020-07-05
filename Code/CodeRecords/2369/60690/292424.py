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
        if str[1]!="*" and str[2]!="*":
            node.left=Node(str[1],None,None)
            node.right=Node(str[2],None,None)
        elif str[1]!="*" and str[2]=="*":
            node.left = Node(str[1], None, None)
        elif str[1]=="*" and str[2]!="*":
            node.right = Node(str[2], None, None)
        else: return
        return
    else:
        add(node.left,str)
        add(node.right,str)

def preorder(node):
    if node==None:return
    print(node.item,end="")
    preorder(node.left)
    preorder(node.right)

n=int(input())
str=input()
t=Tree(Node(str[0],Node(str[1],None,None),Node(str[2],None,None)))

for i in range(n-1):
    str=input()
    add(t.root,str)

preorder(t.root)