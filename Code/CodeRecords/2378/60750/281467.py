class Edge:
    def __init__(self,value,begin,end):
        self.value = value
        self.begin = begin
        self.end = end


def solve():
    tmp = input()
    line1 = []
    if tmp.endswith(' '):
        line1 = list(map(int,tmp[0:len(tmp) - 1].split(' ')))
    else:
        line1 = list(map(int,tmp.split(' ')))
    n = line1[0]
    m = line1[1]
    cost = []
    s = 0
    ways = [[100000000 for j in range(n)] for i in range(n)]
    for i in range(m):
        line2 = list(map(int,input().split(' ')))
        ways[line2[0] -1][line2[1] - 1] = line2[2]
        ways[line2[1] - 1][line2[0] -1] = line2[2]
        s += line2[2]

    edges = []
    low_cost = [100000 for i in range(n)]
    near_vex = [-1 for i in range(n)]
    for i in range(1, n):
        low_cost[i] = ways[0][i]
        near_vex[i] = 0

    mst = Edge

    for i in range(1,n):
        min_cost = 1000000
        v = 0
        for j in range(1,n):
            if near_vex[j] != -1 and low_cost[j] < min_cost:
                v = j
                min_cost = low_cost[j]
        if v > 0:
            mst.value = low_cost[v]
            mst.end = near_vex[v] + 1
            mst.begin = v + 1

            edges.append(mst)
            near_vex[v] = -1
            cost.append(min_cost)

            for j in range(1,n):
                if near_vex[j] != -1 and ways[v][j] < low_cost[j]:
                    low_cost[j] = ways[v][j]
                    near_vex[j] = v
    print(s - sum(cost),end='')


solve()