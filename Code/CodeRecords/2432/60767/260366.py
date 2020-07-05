class Node:
    def __init__(self, value, leftchild=None, rightchild=None):
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.value = value


def makeTree(ins, pos):
    if (len(pos) == 0):
        return None
    root = Node(pos[-1])  # 根是后序遍历的倒数第一个值
    x = 0
    while ins[x] != pos[-1]:
        x += 1
    root.leftchild = makeTree(ins[:x], pos[:x])
    root.rightchild = makeTree(ins[x + 1:], pos[x:-1])
    return root


def dfs(root, sum, leaves):  # leaves存储叶子节点
    if (root == None):
        return
    sum += root.value
    if(root.leftchild == None and root.rightchild == None): #找到叶子节点了
        leaves.append([sum,root.value])
    if(root.leftchild != None):
        dfs(root.leftchild,sum,leaves)
    if(root.rightchild != None):
        dfs(root.rightchild,sum,leaves)

temp = input().split()
ins = []
for t in temp:
    ins.append(int(t))
temp = input().split()
pos = []
for t in temp:
    pos.append(int(t))
leaves = []
sum = 0
root = makeTree(ins,pos)
dfs(root,sum,leaves)
leaves.sort()
print(leaves[0][1])

