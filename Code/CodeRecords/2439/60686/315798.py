class Edge:
    def __init__(self, point1, point2, weight):
        self.point1 = point1
        self.point2 = point2
        self.weight = weight


def go(G, s, S = set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u - 1].difference(P, S):
            Q.add(v)
            P[v] = u
    return P


nums = int(input())
list_all = []
list_temp = []
for i in range(1, nums + 1):
    list_all.append(set())
for i in range(nums - 1):
    info = input().split()
    info = [int(x) for x in info]
    list_all[info[0] - 1].add(info[1])
    list_all[info[1] - 1].add(info[0])
    edge = Edge(info[0], info[1], info[2])
    list_temp.append(edge)
num_ask = int(input())
ask_list = []
for i in range(num_ask):
    ask = input().split()
    ask = [int(x) for x in ask]
    ask_list.append(ask)
for i in range(num_ask):
    ask = ask_list[i]
    startNode = ask[0]
    endNode = ask[1]
    P = go(list_all, startNode)
    weight_list = []
    while P[endNode] is not None:
        tempNode = P[endNode]
        for ch in list_temp:
            if (ch.point1 == endNode and ch.point2 == tempNode) or (ch.point1 == tempNode and ch.point2 == endNode):
                weight_list.append(ch.weight)
                break
        endNode = tempNode
    res = 0
    for ch in weight_list:
        res = res ^ ch
    print(res)