class Edge:
    left = None
    right = None
    graph = None

    def __init__(self, x, y, g):
        self.left = x
        self.right = y
        self.graph = g

    def union_left(self):
        result = [self.left]
        start = 0
        while True:
            n = len(result)
            for i in range(start, len(result)):
                for j in range(1, len(self.graph)):
                    if self.graph[result[i]][j] != 0 and j != self.right and j not in result:
                        result.append(j)
            if n == len(result):
                break
            else:
                start = n
        return result

    def union_right(self):
        result = [self.right]
        start = 0
        while True:
            n = len(result)
            for i in range(start, len(result)):
                for j in range(1, len(self.graph)):
                    if self.graph[result[i]][j] != 0 and j != self.left and j not in result:
                        result.append(j)
            if n == len(result):
                break
            else:
                start = n
        return result

    def delete_left(self):
        result = self.union_left()
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                if i in result or j in result:
                    graph[i][j] = 0

    def delete_right(self):
        result = self.union_right()
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                if i in result or j in result:
                    graph[i][j] = 0

    def beauty_value(self, values):
        lefts = self.union_left()
        rights = self.union_right()
        left_value = 0
        right_value = 0
        for i in range(0, len(lefts)):
            left_value += values[lefts[i]]
        for i in range(0, len(rights)):
            right_value += values[rights[i]]
        return [left_value, right_value]


if __name__ == '__main__':
    n = int(input())
    values = [0] + list(map(int, input().strip().split(" ")))
    graph = [[0 for i in range(0, n + 1)] for j in range(0, n + 1)]
    data = []
    edges = []

    for i in range(0, n - 1):
        x, y = map(int, input().strip().split(" "))
        graph[x][y] = 1
        graph[y][x] = 1
        data.append([x, y])

    for i in range(0, n - 1):
        edge = Edge(data[i][0], data[i][1], graph)
        edges.append(edge)

    vertices = list(range(1, n + 1))
    result = 0

    while True:
        n = len(edges)
        edge_deleted = None
        for edge in edges:
            if edge.left not in vertices or edge.right not in vertices:
                edges.remove(edge)
                continue
            else:
                if min(edge.beauty_value(values)) < 0:
                    if edge_deleted is None:
                        edge_deleted = edge
                    else:
                        if min(edge.beauty_value(values)) < min(edge_deleted.beauty_value(values)):
                            edge_deleted = edge
        if edge_deleted is not None:
            if edge_deleted.beauty_value(values)[0] > 0:
                nums = edge_deleted.union_right()
                edge_deleted.delete_right()
                for num in nums:
                    if num in vertices:
                        vertices.remove(num)
            else:
                nums = edge_deleted.union_left()
                edge_deleted.delete_left()
                for num in nums:
                    if num in vertices:
                        vertices.remove(num)
            edges.remove(edge_deleted)

        if n == len(edges):
            break
        else:
            n = len(edges)

    for vertice in vertices:
        result += values[vertice]
    print(result, end="")
