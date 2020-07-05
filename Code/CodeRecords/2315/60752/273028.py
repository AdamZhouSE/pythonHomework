
def findindex(tree,name):
    nodes=[]
    for t in range(len(tree)):

        if str(tree[t][0])==str(name):nodes.append(t)
    if len(nodes)==0:return -1
    return nodes


def loop(tree,node,count):
    rs=count
    if findindex(tree,node)==-1:return count
    for n in findindex(tree,node):
        rs=max(rs,loop(tree,tree[n][1],count+1))
    return rs


tree=[]
for node in range(int(input())-1):
    tree.append(list(map(int,input().split())))
startnode=[]
for node in tree:
    if startnode.count(node[0])==0:startnode.append(node[0])
root=None
for sn in startnode:
    found=True
    for node in tree:
        if sn==node[1]:
            found=False
            break
    if found:root=sn
print(loop(tree,root,1))

