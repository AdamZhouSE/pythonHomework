class Node:

    def __init__(self, id, child,minn=0,s=0,cost = 0,father = None):
        self.child = child
        self.id = id
        self.minn = minn  #minn记录节点及其子树中需要花费最少的值
        self.father = father
        self.s = s  #s记录节点及其子树中装饰数量
        self.cost = cost  #cost记录满足条件需要的最小花费

    def add(self, node):
        self.child.append(node)


def find(node, target):
    for i in node:
        if i.id == target:
            return i

def dfs(root):
    for i in root.child:
        dfs(i)
        root.minn = min(root.minn,i.minn)
        root.s += i.s
        root.cost += i.cost
    temp = D[root.id] - root.s
    if(temp>0):
        root.s = D[root.id]
        root.cost += root.minn*temp

n = int(input())
node = []
test = []
C = [0]*(n+1)
D = [0]*(n+1)
for i in range(1, n + 1):
    node.append(Node(i,[]))
for i in range(n):
    temp = input().split()
    if(int(temp[0])!=-1):
        find(node, int(temp[0])).add(find(node, i + 1))
    D[i + 1] = int(temp[1])
    C[i + 1] = int(temp[2])
for i in range(1,n+1): #初始化每个节点及其子树中需要花费最少的值为该节点的值
    find(node,i).minn = C[i]
dfs(find(node,1))
print(find(node,1).cost)