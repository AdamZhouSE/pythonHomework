class Node:
    def __init__(self,no, value):
        self.no = no
        self.value = value
        self.son = []

    def left(self):
        if len(self.son) < 1:
            return None
        return self.son[0]

    def right(self):
        if len(self.son) < 2:
            return None
        return self.son[1]

    def setSon(self, node):
        if len(self.son) < 2:
            self.son.append(node)
        else:
            print("fail to set")

    def setValue(self, value):
        self.value = value


def LRV(node, ask):
    if node == None:
        return None
    elif ask == node.no:
        return node.value
    else:
        temp = LRV(node.left(), ask)
        if temp != None:
            return node.value ^ temp
        temp = LRV(node.right(), ask)
        if temp != None:
            return node.value ^ temp
        return None


def solve(pro, root):
    for p in range(pro):
        temp = input().split(' ')
        result = LRV(root, int(temp[0]))
        result = result ^ LRV(root, int(temp[1]))
        print(result)


# main-----
n = int(input())

tree = {}
rootSet = []

for x in range(n - 1):
    temp = input().split(' ')
    father = None
    son = None


    if int(temp[0]) in tree:
        father = tree[int(temp[0])]
    else:
        father = Node(int(temp[0]), 0)
        tree[father.no] = father
    if int(temp[1]) in tree:
        son = tree[int(temp[1])]
        son.setValue(int(temp[2]))
    else:
        son = Node(int(temp[1]), int(temp[2]))
        tree[son.no] = son

    father.setSon(son)

    rootSet.append(father.no)
    if son.no in rootSet:
        rootSet.remove(son.no)

root = rootSet[0]
problem = int(input())
solve(problem, tree[root])

