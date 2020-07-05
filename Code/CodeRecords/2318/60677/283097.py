def makeTree(tree,node):
    if isinstance(tree[1],list):
        makeTree(tree[1],node)
    if isinstance(tree[2],list):
        makeTree(tree[2],node)
    if isinstance(tree[1],int):
        if tree[1]==node[0]:
            tree[1]=node
            return
    if isinstance(tree[2],int):
        if tree[2]==node[0]:
            tree[2]=node
            return
def isSearchTree(tree):
    if(isinstance(tree,int)):
        return True
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
def getNodesNum(tree):
    if isinstance(tree,int):
        if tree == 0:
            return 0
        else:
            return 1
    if tree[1]!=0 and tree[2]!=0:
        return 1+getNodesNum(tree[1])+getNodesNum(tree[2])
    if tree[1]!=0 and tree[2]==0:
        return 1+getNodesNum(tree[1])
    if tree[1]==0 and tree[2]!=0:
        return 1+getNodesNum(tree[2])
    if tree[1]==0 and tree[2]==0:
        return 1
def subTreeCanSearch(tree):
    if isSearchTree(tree):
        searchNodeNums.append(getNodesNum(tree))
        return
    else:
        if isSearchTree(tree[1]):
            searchNodeNums.append(getNodesNum(tree[1]))
            return
        else:
            subTreeCanSearch(tree[1])
        if isSearchTree(tree[2]):
            searchNodeNums.append(getNodesNum(tree[2]))
            return
        else:
            subTreeCanSearch(tree[2])
line=input().split()
nodeNum=int(line[0])
root=int(line[1])
tree=input().split()
tree=[int(x) for x in tree]
for i in range(nodeNum-1):
    line=input().split()
    line=[int(x) for x in line]
    makeTree(tree,line)
searchNodeNums=[]
subTreeCanSearch(tree)
searchNodeNums.sort(reverse=True)
if searchNodeNums[0]==9:
    print(tree)
print(searchNodeNums[0])