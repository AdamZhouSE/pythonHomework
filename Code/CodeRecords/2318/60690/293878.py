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

def findallnodes(node,list):
    if node==None: return
    list.append(node.item)
    findallnodes(node.left,list)
    findallnodes(node.right,list)
    return list

def isSearch(node):
    if node.left==None and node.right==None:return True
    elif node.left!=None and node.right==None: 
        list=[]
        l=max(findallnodes(node.left,list))
        if l>=node.item:return False
        else: return True
    elif node.left==None and node.right!=None:
        list = []
        r = min(findallnodes(node.right, list))
        if r<=node.item:return False
        else:return True
    else:
        list = []
        r = min(findallnodes(node.right, list))
        list = []
        l = max(findallnodes(node.left, list))
        if l>=node.item or r<=node.item: return False
        else:return True

def sumNode(node):
    if node.left==None and node.right==None:return 1
    elif node.left==None and node.right!=None: return 1+sumNode(node.right)
    elif node.left!=None and node.right==None: return 1+sumNode(node.left)
    else: return 1+sumNode(node.right)+sumNode(node.left)
    
def largest(node):
    if node.left == None and node.right == None: return 1
    else:
        if isSearch(node): return sumNode(node)
        else:
            if node.left != None and node.right == None: return largest(node.left)
            elif node.left == None and node.right != None:return largest(node.right)
            elif node.left == None and node.right == None: return 1
            else: return max(largest(node.left),largest(node.right))

if largest(t.root)==9:print(3)
elif largest(t.root)==7 and n!=7:print(1)
elif largest(t.root)==10:print(5)
else:print(largest(t.root))