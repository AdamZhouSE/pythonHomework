class Node:
    def __init__(self,num,father):
        self.val=num
        self.father=father
def getIndex(n,l):
    for i in range(len(l)):
        if l[i][0]==n:
            return i
def getDex(l, n):
    for i in range(len(l)):
        if l[i].val == n:
            return l[i]
    return None
def getTree(l,n,root,leaf):
    a=getIndex(n,l)
    b=l[a][1]
    c=l[a][2]

    if b!=0:
        n1=Node(b,root)
        leaf.append(n1)
        #print(root.left.val)
        #r.append(n1)
    if c != 0:
        n2 = Node(c, root)
        leaf.append(n2)
        #r.append(n2)
    if b!=0: n1=getTree(l, b, n1,leaf)
    if c!=0: n2=getTree(l, c, n2,leaf)
    return root
l=input().split(" ")
n1=int(l[0])
n2=int(l[1])
all=[]
leaf=[]
for i in range(n1):
    l1=input().split(" ")
    for j in range(len(l1)):
        l1[j]=int(l1[j])
    all.append(l1)
check=input().split(" ")
c1=int(check[0])
c2=int(check[1])
root=Node(n2,None)
leaf.append(root)
#print(root.left.val)
root=getTree(all,n2,root,leaf)
node1=getDex(leaf,c1)
node2=getDex(leaf,c2)
flag=0
fa1=[]
fa2=[]
while(node1!=None or node2!=None):
    if node1!=None:
        fa1.append(node1)
    if node2!=None:
        fa2.append(node2)
    if node1!=None:
        node1=node1.father
    if node2!=None:
        node2=node2.father
for i in range(len(fa1)):
    if flag==1:
        break
    for j in range(len(fa2)):
        if fa1[i].val==fa2[j].val:
            print(fa1[i].val)
            flag=1
            break