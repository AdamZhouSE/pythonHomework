def main():
    num_of_vertices = int(input())
    graph = [[0 for a in range(0, num_of_vertices + 1)] for j in range(0, num_of_vertices + 1)]
    orzFangs = [0] + list(map(int, input().split(" ")))
    destinations = [0] + list(map(int, input().split(" ")))
    for i in range(1, num_of_vertices + 1):
        graph[i][destinations[i]] = 1

    for i in range(1, num_of_vertices + 1):
        paths = find_path(i, graph)
        results = [0 for a in range(0, len(paths))]
        for j in range(0, len(paths)):
            for k in range(0, len(paths[j])):
                results[j] += orzFangs[paths[j][k]]
        print(max(results))


def find_path(start, graph):
    choices = [[start]]
    start = 0
    while True:
        n = len(choices)
        for i in range(start, n):
            past = choices[i][len(choices[i]) - 1]
            for j in range(1, len(graph)):
                if graph[past][j] == 1 and j not in choices[i]:
                    choices.append(choices[i] + [j])
        if n == len(choices):
            break
        else:
            start = n
    return choices


if __name__ == '__main__':
    main()
