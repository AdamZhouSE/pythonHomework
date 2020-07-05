def find_path(start, end, graph):
    choices = [[start]]
    result = []
    while True:
        n = len(choices)
        for i in range(0, n):
            past = choices[i][len(choices[i]) - 1]
            if past != end:
                for j in range(1, len(graph)):
                    if graph[past][j] != 0:
                        if j == end:
                            result.append(choices[i] + [j])
                        elif j not in choices[i]:
                            choices.append(choices[i] + [j])
        if n == len(choices):
            break
        else:
            choices = choices[n:]
    return result


if __name__ == '__main__':
    num_of_vertices = int(input())
    graph = [[0 for i in range(0, num_of_vertices + 1)] for j in range(0, num_of_vertices + 1)]
    for i in range(0, num_of_vertices - 1):
        x, y, weight = map(int, input().split(" "))
        graph[x][y] = weight
    num_of_questions = int(input())
    for i in range(0, num_of_questions):
        start, end = map(int, input().split(" "))
        result = find_path(start, end, graph)
        if len(result) == 0:
            print(0)
        else:
            temp = graph[result[0][0]][result[0][1]]
            for j in range(1, len(result[0]) - 1):
                temp = temp ^ graph[result[0][j]][result[0][j + 1]]
            print(temp)
