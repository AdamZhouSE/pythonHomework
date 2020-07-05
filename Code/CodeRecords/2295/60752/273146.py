
def findindex(tree,name):
    for t in range(len(tree)):

        if str(tree[t][0])==str(name):return t
    return -1



def loop(fatherlist,node1,node2):
    father1=fatherlist[findindex(fatherlist,node1)][1]
    father2 = fatherlist[findindex(fatherlist, node2)][1]
    if father1==father2:return father1
    else:return loop(fatherlist,father1,father2)

tree=[]
inp=input().split()
root=int(inp[1])
for node in range(int(inp[0])):
    tree.append(list(map(int,input().split())))
fatherlist=[]
for  node in tree:
    if node[1]!=0:fatherlist.append([node[1],node[0]])
    if node[2] != 0: fatherlist.append([node[2], node[0]])
line=input().split()
node1=int(line[0])
node2=int(line[1])
fathers1=[]
fathers2=[]
index=findindex(fatherlist,node1)
while index!=-1:
    fathers1.append(node1)
    node1=fatherlist[index][1]
    index=findindex(fatherlist,node1)
index=findindex(fatherlist,node2)
while index!=-1:
    fathers2.append(node2)
    node2=fatherlist[index][1]
    index=findindex(fatherlist,node2)
    
fathers1.append(root)
fathers2.append(root)
found=False
for i in fathers1:
    for j in fathers2:
        if i==j:
            found=True
            print(i)
            break
    if found:break



