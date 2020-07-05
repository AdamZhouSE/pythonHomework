"""
最小生成树
"""
class Edge:
    def __init__(self):
        self.start = 0
        self.to = 0
        self.length = 0


edges = []
vertexes = []


def solve(n):
    edges.sort(key=lambda x: x.length)
    i = 0
    cnt = 0
    while True:
        if not (vertexes.__contains__(edges[i].to) and vertexes.__contains__(edges[i].start)):
            if not vertexes.__contains__(edges[i].start):
                vertexes.append(edges[i].start)
            if not vertexes.__contains__(edges[i].to):
                vertexes.append(edges[i].to)
            cnt += 1
            if cnt == n-1:
                return edges[i].length
        i += 1


if __name__ == '__main__':
    arr = [int(j) for j in input().split()]
    n = arr[0]
    m = arr[1]
    edges = [Edge() for i in range(m)]
    for i in range(m):
        arr = [int(j) for j in input().split()]
        edges[i].start = arr[0]
        edges[i].to = arr[1]
        edges[i].length = arr[2]
    print(solve(n), end='')