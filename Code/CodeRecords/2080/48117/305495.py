questNum = int(input())

for quest in range(questNum):
    ns = input().split(' ')
    n = int(ns[0])
    start = ns[1]
    s = input().split(' ')

    graph = []
    for i in range(n):
        s1 = input().split(' ')
        start1 = s1[0]
        for j in range(1, n + 1):
            if s1[j] == '1':
                if (not (start1, s[j - 1]) in graph) or (not (s[j - 1], start) in graph):
                    graph.append((start1, s[j - 1]))

    print(graph)

    next = start
    while len(graph) > 0:
        for i in range(len(graph)):
            if graph[i][0] == next:
                print(graph[i][0], end=' ')
                next = graph[i][1]
                del graph[i]
                break

    print()