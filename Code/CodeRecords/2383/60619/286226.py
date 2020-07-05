class Node:
    def __init__(self, v, son):
        self.value = v
        self.children = [son]
        self.totalNum = 1


def getNode(target):
    for tn in treeNodes:
        if tn.value == target:
            return tn


def updateChildren():
    tempI = len(treeNodes) - 1
    while tempI >= 0:
        temp = treeNodes[tempI]
        temp.totalNum = 1
        for val in temp.children:
            if val in values:
                temp.totalNum += treeNodes[values.index(val)].totalNum
            else:
                temp.totalNum += 1
        tempI -= 1


t = int(input())
for ind in range(t):
    li = input().strip().split(" ")
    n = int(li[0])
    k = int(li[1])
    treeNodes = []
    values = []

    # 完成对于输入的初始化
    for i in range(n - 1):
        l = input().strip().split(" ")
        va = int(l[0])
        so = int(l[1])
        if va not in values:
            treeNodes.append(Node(va, so))
            values.append(va)
        else:
            getNode(va).children.append(so)

    # 更新子结点个数
    updateChildren()

    # 开始循环判断是否能切割成子树
    result = True
    while len(treeNodes)>0:
        for tn in treeNodes:
            if tn.totalNum == k:
                for s in tn.children:
                    if s in values:
                        del(treeNodes[values.index(s)])
                        del(values[values.index(s)])
                del (treeNodes[treeNodes.index(tn)])
                del (values[values.index(tn.value)])
                for e in treeNodes:
                    if tn.value in e.children:
                        del (e.children[e.children.index(tn.value)])
                break
        else:
            result = False

        # 再次更新子节点的数量
        if not result:
            break
        else:
            updateChildren()

    if result:
        print("YES")
    else:
        print("NO")