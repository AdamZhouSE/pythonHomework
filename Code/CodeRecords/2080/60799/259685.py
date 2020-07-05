class Graph(object):
    def __init__(self, value):
        self.value = value
        self.linkedSet = []
        self.visit = False

    def __str__(self):
        return str(self.value)

    def add(self, other):
        """
        :type other: Graph
        """
        self.linkedSet.append(other)
        other.linkedSet.append(self)


T = int(input())
for ttt in range(T):
    inner = input().strip().split()
    n = int(inner[0])
    start = inner[1]
    graphList = [Graph(i) for i in input().strip().split()]
    dict1 = {}
    for i in range(len(graphList)):
        dict1[graphList[i].value] = i
    for iii in range(n):
        inner = input().strip().split()
        g0 = graphList[dict1[inner.pop(0)]]
        inner = [int(i) for i in inner]
        for j in range(len(inner)):
            if inner[j] == 1:
                g0.add(graphList[j])
    start = [i for i in graphList if i.value == start][0]
    List, res = [start], []
    start.visit = True
    while List:
        res += List
        tmp = []
        for i in List:
            for j in i.linkedSet:
                if not j.visit:
                    j.visit = True
                    tmp.append(j)
        List = tmp
    print(' '.join([str(i) for i in res]))