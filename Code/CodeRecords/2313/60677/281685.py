def makeTree(tree,nodes):
    nodes=list(nodes)
    if nodes.__len__()==0 or isinstance(tree,int):
        return
    if(isinstance(tree[1],int)):
        for i in nodes[:]:
            if i[0]==tree[1]:
                tree[1]=i
                nodes.remove(i)
                break
        makeTree(tree[1],nodes)
    if(isinstance(tree[2],int)):
        for i in nodes[:]:
            if i[0]==tree[2]:
                tree[2]=i
                nodes.remove(i)
                break
        makeTree(tree[2],nodes)
def isSearchTree(tree):
    if(isinstance(tree[2],list)and isinstance(tree[1],list)):
        if tree[1][0]>=tree[0] or tree[2][0]<=tree[0]:
            return False
        else:
            return isSearchTree(tree[1]) and isSearchTree(tree[2])
    elif(isinstance(tree[1],list) and isinstance(tree[2],int)):
        if tree[1][0]>=tree[0]:
            return False
        elif tree[2]!=0 and tree[2]<=tree[0]:
            return False
        else:
            return isSearchTree(tree[1])
    elif(isinstance(tree[2],list)and isinstance(tree[1],int)):
        if tree[2][0]<=tree[0]:
            return False
        elif tree[1]!=0 and tree[1]>=tree[0]:
            return False
        else:
            return isSearchTree(tree[2])
    else:
        if tree[2]!=0 and tree[2]<=tree[0]:
            return False
        elif tree[1]!=0 and tree[1]>=tree[0]:
            return False
        return True

def isComplete(tree):
    for i in range((treeArray.__len__()-1)//2):
        if treeArray[i]==tree[0]:
            if isinstance(tree[1],list):
                treeArray[i*2+1]=tree[1][0]
                isComplete(tree[1])
            if isinstance(tree[2],list):
                treeArray[i*2+2]=tree[2][0]
                isComplete(tree[2])
            if isinstance(tree[1], int) or isinstance(tree[2], int):
                if isinstance(tree[1], int):
                    treeArray[i*2+1]=tree[1]
                if isinstance(tree[2], int):
                    treeArray[i * 2 + 2] = tree[2]
                return
            break

line=input().split()
n=int(line[0])
root=int(line[1])
set={root}
nodes=[]
tree=[]
while True:
    line=input().split()
    line=[int(x) for x in line]
    for i in line:
        if i!=0:
            set.add(i)
    nodes.append(line)
    if set.__len__()==n:
        break
for i in nodes[:]:
    if i[0]==root:
        tree=i
        nodes.remove(i)

makeTree(tree,nodes)
treeArray=[0 for x in range((2**n)*2+1)]
treeArray[0]=tree[0]
if(isSearchTree(tree)):
    print("true")
else:
    print("false")
isComplete(tree)
treeArray.reverse()
complete=True
for i in range(treeArray.__len__()):
    if i!=0:
        for j in range(i+1,treeArray.__len__()):
            if i==0:
                complete=False
                break
        break
if not isSearchTree(tree) and complete:
    print(n,root,nodes)
if complete:
    print("true")
else:
    print("false")