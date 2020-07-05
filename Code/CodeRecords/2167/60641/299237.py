def main():
    n, m, L = map(int, input().split(" "))
    colors = list(map(int, input().split(" ")))
    colors = [max(colors) + L + 1] + colors
    graph = [[10000 for i in range(0, n + 1)] for j in range(0, n + 1)]
    for i in range(0, m):
        x, y, weight = map(int, input().split(" "))
        graph[x][y] = weight
        graph[y][x] = weight
    colors_combinations = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if abs(colors[i] - colors[j]) >= L:
                colors_combinations.append([i, j])
    result = 0
    for i in range(0, len(colors_combinations)):
        paths = find_path(colors_combinations[i][0], colors_combinations[i][1], graph)
        result += min(paths)
    print(result)


def find_path(start, end, graph):
    choices = [[start]]
    result = []
    while True:
        n = len(choices)
        for i in range(0, n):
            past = choices[i][len(choices[i]) - 1]
            if len(choices[i]) == 1 or past != end:
                for j in range(1, len(graph)):
                    if graph[past][j] != 10000 and j not in choices[i]:
                        if j == end:
                            d = 0
                            temp = choices[i] + [j]
                            for k in range(0, len(choices[i])):
                                d = max(d, graph[temp[k]][temp[k + 1]])
                            result.append(d)
                        elif j not in choices[i]:
                            choices.append(choices[i] + [j])
        if n == len(choices):
            break
        else:
            choices = choices[n:]
    return result


if __name__ == '__main__':
    main()
