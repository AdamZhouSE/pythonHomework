class TreeNode:
    def __init__(self,value):
        self.value = value
        self.lch = None
        self.rch = None

    def setlch(self,node):
        self.lch = node

    def setrch(self,node):
        self.rch = node


def weights(root,h):
    if root.rch is None and root.lch is None:
        return root.value*h
    else:
        weight = weights(root.rch,h+1)
        weight = weight + weights(root.lch,h+1)
        return weight


def takevalue(element):
    return element.value


n = int(input())
source = input().split(' ')
nodes = []
for a in range(0,n):
    nodes.append(TreeNode(int(source[a])))
while len(nodes)>1:
    node1 = min(nodes,key=takevalue)
    nodes.remove(node1)
    node2 = min(nodes,key=takevalue)
    nodes.remove(node2)
    newnode = TreeNode(node1.value+node2.value)
    newnode.setlch(node1)
    newnode.setrch(node2)
    nodes.append(newnode)
result = weights(newnode,0)
print(result)









