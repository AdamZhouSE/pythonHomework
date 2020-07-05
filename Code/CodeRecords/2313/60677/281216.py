def makeTree(tree,nodes):
    nodes=list(nodes)
    if nodes.__len__()==0:
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
        isSearchTree(tree[1])
        isSearchTree(tree[2])
    elif(isinstance(tree[1],list) and isinstance(tree[2],int)):
        if tree[1][0]>=tree[0]:
            return False
        if tree[2]!=0 and tree[2]<=tree[0]:
            return False
        isSearchTree(tree[1])
    elif(isinstance(tree[2],list)and isinstance(tree[1],int)):
        if tree[2][0]<=tree[0]:
            return False
        if tree[1]!=0 and tree[1]>=tree[0]:
            return False
        isSearchTree(tree[2])
    else:
        if tree[2]!=0 and tree[2]<=tree[0]:
            return False
        if tree[1]!=0 and tree[1]>=tree[0]:
            return False
        return True
def isComplete(tree):
    if(isinstance(tree[2],list)and isinstance(tree[1],list)):
        if tree[1][1]==0 or tree[1][2]==0:
            return False
        isComplete(tree[1])
        isComplete(tree[2])
    elif(isinstance(tree[1],list) and isinstance(tree[2],int)):
        if tree[2]==0:
            if tree[1][1]==0 and tree[1][2]!=0:
                return False
        else:
            if tree[1][1]==0 or tree[1][2]==0:
                return False
        isComplete(tree[1])
    elif(isinstance(tree[2],list)and isinstance(tree[1],int)):
        if tree[1]==0:
            return False
        if tree[2][1] == 0 and tree[2][2] != 0:
            return False
        isComplete(tree[2])
    else:
        if tree[1]==0 and tree[2]!=0:
            return False
        return True
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
try:
    makeTree(tree,nodes)
except:
    print(nodes)
if(isSearchTree(tree)):
    print("true")
else:
    print("false")
if(isComplete(tree)):
    print("true")
else:
    print("false")