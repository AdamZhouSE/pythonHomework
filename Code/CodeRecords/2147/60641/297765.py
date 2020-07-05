def main():
    n, m, k, a, b = map(int, input().split(" "))
    graph = [[10000 for i in range(0, n + 1)] for j in range(0, n + 1)]
    for i in range(0, m):
        x, y = map(int, input().split(" "))
        graph[x][y] = a
        graph[y][x] = a

    new_edges = []
    for i in range(1, n + 1):
        paths = shortest_path(n, i, graph)
        try:
            while True:
                j = paths.index(2 * a)
                paths[j] = 10000
                new_edge = [min(i, j), max(i, j)]
                if new_edge not in new_edges:
                    new_edges.append(new_edge)
        except ValueError:
            pass
    for i in range(0, len(new_edges)):
        if graph[new_edges[i][0]][new_edges[i][1]] == 10000:
            graph[new_edges[i][0]][new_edges[i][1]] = b
            graph[new_edges[i][1]][new_edges[i][0]] = b

    paths = shortest_path(n, k, graph)
    paths[k] = 0
    for i in range(1, n + 1):
        print(paths[i])


def shortest_path(n, k, graph):
    times = [10000] * (n + 1)
    able_to_change = [True] * (n + 1)
    past = [k for a in range(n + 1)]
    for j in range(1, n + 1):
        times[j] = graph[k][j]
    able_to_change[k] = False

    for j in range(1, n):
        next_point = 0
        for k in range(1, n + 1):
            if able_to_change[k] and times[k] != 10000:
                if next_point == 0:
                    next_point = k
                else:
                    if times[k] < times[next_point]:
                        next_point = k
        able_to_change[next_point] = False
        for k in range(1, n + 1):
            if able_to_change[k] and times[k] > times[next_point] + graph[next_point][k]:
                times[k] = times[next_point] + graph[next_point][k]
                past[k] = next_point

    return times


if __name__ == '__main__':
    main()
