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

str=input().split(" ")
n=int(str[0])
roo=int(str[1])

nodes=[]
for i in range(n):
    str=input().split(" ")
    item=int(str[0])
    l=int(str[1])
    r=int(str[2])
    nodes.append([item,l,r])


t=Tree
for j in range(len(nodes)):
    if nodes[j][0] == roo:
        t=Tree(Node(nodes[j][0],Node(nodes[j][1],None,None),Node(nodes[j][2],None,None)))


for i in range(len(nodes)):
    if nodes[i][0]!=roo:add(t.root,nodes[i])

def isSearch(node):
    if node.left==None and node.right==None:return True
    elif node.left==None and node.item<node.right.item: return isSearch(node.right)
    elif node.right==None and node.item>node.left.item: return isSearch(node.left)
    elif node.left==None and node.item>node.right.item: return False
    elif node.right==None and node.item<node.left.item: return False
    elif node.item>node.left.item and node.item<node.right.item:
        return isSearch(node.left) and isSearch(node.right)
    else: return False

def isComp(node,height,exp):
    if height<exp:
        if node.left==None or node.right==None:
            return False
        else:
            return isComp(node.left,height+1,exp) and isComp(node.right,height+1,exp)
    else: return True

def findDeep(node,deep):
    if node.left!=None and node.right!=None:return max(findDeep(node.left,deep+1),findDeep(node.right,deep+1))
    elif node.left==None and node.right!=None:return findDeep(node.right,deep+1)
    elif node.left != None and node.right == None: return findDeep(node.left, deep + 1)
    else: return deep

exp=findDeep(t.root,0)

if isSearch(t.root):print("true")
else:print("false")
if isComp(t.root,0,exp-1):print("true")
else:print("false")
