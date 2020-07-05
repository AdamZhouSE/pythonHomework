class Graph(object):
    def __init__(self, value):
        self.value = value
        self.linkedSet = []
        self.color = 0

    def __str__(self):
        return str(self.value)

    def add(self, other):
        """
        :type other: Graph
        """
        self.linkedSet.append(other)
        other.linkedSet.append(self)

    def conflict(self, lim):
        if lim == 0:
            if self.color == 0:
                self.color = 1
                for i in self.linkedSet:
                    if i.conflict(self.color):
                        return True
                return False
            else:
                return False
        else:
            if lim == self.color:
                return True
            elif lim+self.color == 0:
                return False
            else:
                self.color = -lim
                for i in self.linkedSet:
                    if i.conflict(self.color):
                        return True
                return False


T = int(input())
for tt in range(T):
    inner = input().strip().split()
    n = int(inner[0])
    m = int(inner[1])
    graphList = [Graph(i) for i in range(n)]
    if m>2+n:
        print('NO')
    else:
        for ttt in range(m):
            inner = [int(i) for i in input().strip().split()]
            i, j = inner[0]-1, inner[1]-1
            graphList[i].add(graphList[j])

        for ii in graphList:
            if ii.conflict(0):
                print('NO')
                break
        else:
            print('YES')
