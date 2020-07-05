def main():
    n = int(input())
    for i in range(0, n):
        num_of_vertices, num_of_edges = map(int, input().split(" "))
        graph = [[0 for a in range(0, num_of_vertices + 1)] for b in range(0, num_of_vertices + 1)]
        for j in range(0, num_of_edges):
            x, y = map(int, input().split(" "))
            graph[x][y] = 1
            graph[y][x] = 1
        result = True

        for j in range(1, num_of_vertices + 1):
            paths = list(set(find_path(j, j, graph)))
            for k in range(0, len(paths)):
                if paths[k] % 2 == 1:
                    result = False
                    break
            if not result:
                break

        if result:
            point_deleted = 0
            edge_deleted = 0
            for j in range(1, num_of_vertices + 1):
                if graph[j].count(1) == 1:
                    k = graph[j].index(1)
                    graph[j][k] = 0
                    graph[k][j] = 0
                    point_deleted += 1
                    edge_deleted += 1
            if (num_of_vertices - point_deleted) % 2 == 0 and num_of_vertices - point_deleted == num_of_edges - edge_deleted:
                pass
            else:
                num = []
                for j in range(1, num_of_vertices + 1):
                    if graph[j].count(1) == 3:
                        if len(num) < 2:
                            num.append(j)
                        else:
                            result = False
                            break
                if len(num) != 2:
                    result = False
                if not result:
                    pass
                else:
                    paths = find_path(num[0], num[1], graph)
                    if paths.count(2) >= 2:
                        paths.remove(2)
                        paths.remove(2)
                        if paths[0] % 2 == 0:
                            pass
                        else:
                            result = False
                    else:
                        result = False

        if num_of_vertices > num_of_edges:
            result = True

        if result:
            print("YES")
        else:
            print("NO")


def find_path(start, end, graph):
    choices = [[start]]
    result = []
    while True:
        n = len(choices)
        for i in range(0, n):
            past = choices[i][len(choices[i]) - 1]
            if len(choices[i]) == 1 or past != end:
                for j in range(1, len(graph)):
                    if graph[past][j] == 1:
                        if j == end:
                            result.append(len(choices[i]))
                        elif j not in choices[i]:
                            choices.append(choices[i] + [j])
        if n == len(choices):
            break
        else:
            choices = choices[n:]
    return result


if __name__ == '__main__':
    main()
