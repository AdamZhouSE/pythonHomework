M_N = input().split(' ')
M = int(M_N[1])
N = int(M_N[0])

graph = []
for i in range(N):
    x = input()
    graph.append(list(x + '*'))

graph.append(list('*' * (len(x) + 1)))

test = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] != '*':
            if graph[i][j] == '2':
                test += 1
                graph[i][j] = '*'
            else:
                if (graph[i][j] == '1' and graph[i][j + 1] == '3') or (graph[i][j] == '3' and graph[i][j + 1] == '1'):
                    test += 1
                    graph[i][j] = '*'
                    graph[i][j + 1] = '*'
                if (graph[i][j] == '1' and graph[i + 1][j] == '3') or (graph[i][j] == '3' and graph[i + 1][j] == '1'):
                    test += 1
                    graph[i][j] = '*'
                    graph[i + 1][j] = '*'

print(test)