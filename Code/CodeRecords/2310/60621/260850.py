class tree:
    value=0
    left=None
    right=None
    def __init__(self,v):
        self.value=v
temp=[int(x) for x in input().split()]
a=temp[0]
headIndex=temp[1]-1
branch=[tree(i) for i in range(100000)]
level=[True for i in range(1000)]
def middleLI(node:tree,depth,path:list):
    global level
    if node.left==None and node.right==None:
        path.append(node.value)
        if level[depth]==True:
            level[depth]=False
        return
    else:
        if level[depth]==True:
            path.append(node.value)
            level[depth]=False
        if node.left!=None:
            middleLI(node.left,depth+1,path)
        if node.right!=None:
            middleLI(node.right,depth+1,path)
    return

def middleRI(node:tree,depth,path:list):
    global level
    if node.left==None and node.right==None:
        path.append(node.value)
        if level[depth]==True:
            level[depth]=False
        return
    else:
        if level[depth]==True:
            path.append(node.value)
            level[depth]=False

        if node.right!=None:
            middleRI(node.right,depth+1,path)
        if node.left!=None:
            middleRI(node.left,depth+1,path)
    return

flag=True
def middleLII(node:tree,depth,path:list):
    global flag
    if node.left==None and node.right==None:
        path.append(node.value)
        flag=False
        return
    else:
        if flag==True:
            path.append(node.value)
        if node.left!=None:
            middleLII(node.left,depth+1,path)
        if node.right!=None:
            middleLII(node.right,depth+1,path)
    return

def middleRII(node:tree,depth,path:list):
    global flag
    if node.left==None and node.right==None:
        path.append(node.value)
        flag=False
        return
    else:
        if flag==True:
            path.append(node.value)

        if node.right!=None:
            middleRII(node.right,depth+1,path)
        if node.left != None:
            middleRII(node.left, depth + 1, path)
    return
for i in range(a):
    temp=[int(x)-1 for x in input().split()]
    if temp[1]!=-1:
        branch[temp[0]].left=branch[temp[1]]
    if temp[2]!=-1:
        branch[temp[0]].right=branch[temp[2]]

head=branch[headIndex]
path1=[headIndex]
path2=[]
middleLI(head.left,1,path1)
level=[True for i in range(1000)]
middleRI(head.right,1,path2)

path3=[headIndex]
path4=[]
middleLII(head.left,1,path3)
flag=True
middleRII(head.right,1,path4)
path2.reverse()
path4.reverse()
for i in path1:
    print(i+1,end=" ")
for i in path2:
    print(i+1,end=" ")
print("",end="\n")
for i in path3:
    print(i+1,end=" ")
for i in path4:
    print(i+1,end=" ")
