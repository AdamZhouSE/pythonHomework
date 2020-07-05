class Node:
    def __init__(self, cost, dang):
        self.son = []
        self.p = None
        self.c = cost
        self.d = dang


num = int(input())
Nodes = [Node(0, 0) for i in range(num)]
for i in range(num):
    temp = input().split(" ")
    p = int(temp[0])
    d = int(temp[1])
    c = int(temp[2])
    Nodes[i].c = c
    Nodes[i].d = d
    if p != -1:
        Nodes[i].p = Nodes[p - 1]
        Nodes[p - 1].son.append(Nodes[i])


def dfs(root):
    if len(root.son) == 0:
        return root.d, root.c, root.d * root.c
    totalnum = 0
    Min = 10000000
    cost = 0
    for n in root.son:
        temp = dfs(n)
        totalnum += temp[0]
        Min = min(Min, temp[1])
        cost += temp[2]
    if totalnum > root.d:
        return totalnum, Min, cost
    else:
        cost += Min * (root.d - totalnum)
        totalnum = root.d
        return totalnum, Min, cost


result = dfs(Nodes[0])
print(result[2])
