"""
@:parameter 存储各边权重的矩阵edge
@:parameter 存储起始点的index v
@:return 起始点v到各点的最短路径
"""


def dijkstra(edge, v):
    n = len(edge)
    distance = [10 ** 10 for _ in range(n)]
    is_visited = [False for _ in range(n)]
    for i in range(0, n):
        distance[i] = edge[v][i]
    is_visited[v] = True

    # 处理从点v到其余点的最短路径
    for _ in range(0, n):
        mini = 10 ** 10
        index = -1
        for j in range(0, n):
            if not is_visited[j]:
                if distance[j] < mini:
                    index = j
                    mini = distance[j]
        if index != -1:
            is_visited[index] = True
        for w in range(0, n):
            if not is_visited[w]:
                if edge[index][w] < 10**9 and mini + edge[index][w] < distance[w]:
                    distance[w] = edge[index][w]
    return distance


if __name__ == '__main__':
    p = []
    [n, q] = list(map(int, input().split(" ")))

    matrix = [[10**10 for _ in range(n)] for _ in range(n)]

    for _ in range(0, q):
        line = list(map(int, input().split(" ")))
        event = line[0]
        island1 = line[1]
        island2 = line[2]

        # 事件0：在x岛和y岛之间建成一座危险系数为v的桥
        if event == 0:
            index = line[3]
            matrix[island1][island2] = index
            matrix[island2][island1] = index

        # 事件1：x岛和y岛之间岛桥没了
        elif event == 1:
            matrix[island1][island2] = 10**10
            matrix[island2][island1] = 10**10

        # 事件2：询问x岛到y岛的危险系数
        else:
            array = dijkstra(matrix, island1)
            if array[island2] > 10 ** 9:
                print(-1)
            else:
                print(array[island2])

