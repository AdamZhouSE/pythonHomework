class Node:
    def __init__(self, no, pi=None, di=0, ci=0, dec=0):
        self.no = no
        self.pi = pi
        self.di = di
        self.ci = ci
        self.dec = dec
        self.children = []


def test():
    n = int(input())
    nodes = [Node(i) for i in range(0, n + 1)]
    okList = [0 for i in range(0,n+1)]
    for i in range(1, n + 1):
        pdc = input().split()
        p = int(pdc[0])
        d = int(pdc[1])
        c = int(pdc[2])
        if p == -1:
            nodes[i].pi = None
        else:
            nodes[i].pi = nodes[p]
            nodes[p].children.append(nodes[i])
        nodes[i].di = d
        nodes[i].ci = c
    decorations = [0] * (n + 1)
    cost = 0
    childList = []
    parentList = []
    while True:
        parentList = []
        for i in range(1, n + 1):
            if able(childList, nodes[i].children) and (okList[i] != 1):
                if nodes[i].dec < nodes[i].di:

                    num=nodes[i].di - nodes[i].dec
                    cost = cost + num * nodes[i].ci
                    nodes[i].dec = nodes[i].di
                    addToParent(nodes[i], num)
                parentList.append(nodes[i])
                okList[i] = 1
        if not parentList:
            break
        childList = parentList
    print(cost)


def able(childList, nodesChildren):
    for child in nodesChildren:
        if child not in childList:
            return False
    return True


def addToParent(nodes, num):
    if nodes.pi is not None:
        nodes.pi.dec += num
        nodes.pi.ci = min(nodes.ci, nodes.pi.ci)
        addToParent(nodes.pi, num)


test()
