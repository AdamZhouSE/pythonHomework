def main():
    num_of_vertices, num_of_edges = map(int, input().split(" "))
    result = 0
    graph = [[10000 for i in range(0, num_of_vertices + 1)] for j in range(0, num_of_vertices + 1)]
    for i in range(0, num_of_edges):
        x, y, weight = map(int, input().split(" "))
        graph[x][y] = min(weight, graph[x][y])
        result += weight
    for i in range(1, num_of_vertices + 1):
        information = shortest_paths(num_of_vertices, i, graph)
        times = information[0]
        past = information[1]
        paths = []
        if times.count(10000) == 2:
            for j in range(1, num_of_vertices + 1):
                if j == i:
                    continue
                else:
                    temp = j
                    while past[temp] != i:
                        if [past[temp], temp] not in paths:
                            paths.append([past[temp], temp])
                        temp = past[temp]
                    if [past[temp], temp] not in paths:
                        paths.append([past[temp], temp])
            weights = 0
            for j in range(0, len(paths)):
                weights += graph[paths[j][0]][paths[j][1]]
            result = min(result, weights)
    print(result)


def shortest_paths(n, start, graph):
    times = [10000] * (n + 1)
    able_to_change = [True] * (n + 1)
    past = [start for a in range(n + 1)]
    for j in range(1, n + 1):
        times[j] = graph[start][j]
    able_to_change[start] = False

    information = shortest_path(n, start, graph)
    for i in range(1, len(information[0])):
        if information[0][i] != 10000 and information[1][i] == start:
            times[i] = graph[start][i]
            able_to_change[i] = False

    for j in range(1, n):
        past_point = 0
        next_point = 0
        for a in range(1, n + 1):
            if not able_to_change[a]:
                for k in range(1, n + 1):
                    if able_to_change[k] and graph[a][k] != 10000:
                        if graph[a][k] < graph[past_point][next_point]:
                            next_point = k
                            past_point = a
        if past_point != 0 and next_point != 0:
            times[next_point] = times[past_point] + graph[past_point][next_point]
            able_to_change[next_point] = False
            past[next_point] = past_point

    return [times, past]


def shortest_path(n, start, graph):
    times = [10000] * (n + 1)
    able_to_change = [True] * (n + 1)
    past = [start for a in range(n + 1)]
    for j in range(1, n + 1):
        times[j] = graph[start][j]
    able_to_change[start] = False

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

    return [times, past]


if __name__ == '__main__':
    main()
