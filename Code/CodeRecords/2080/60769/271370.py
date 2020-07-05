def bfs(graph, point, start):
    visited = [False] * len(point)
    stack = [start]
    visited[start] = True
    res = []
    while len(stack) != 0:
        now = stack.pop(0)
        res.append(point[now])
        for i in range(len(point)):
            temp = graph[now][i]
            if temp == 1 and not visited[i]:
                stack.append(i)
                visited[i] = True
    return res


if __name__ == '__main__':
    num = int(input())
    for j in range(num):
        graph = []
        n, start = input().split()
        n = int(n)
        point = input().split()
        for i in range(n):
            graph.append(list(map(int, input().split()[1:])))
        res = bfs(graph, point, point.index(start))
        print(" ".join(res))