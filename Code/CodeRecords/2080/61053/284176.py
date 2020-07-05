def bfs(graph:list,start,names:list):
    outOrder = [names.index(start)]
    lastvisit = [start.index(start)]
    while lastvisit != []:
        newvisit = []
        for node in lastvisit:
            for j in range(len(graph[node])):
                if graph[node][j]==1 and not (j in outOrder):
                    outOrder.append(j)
                    newvisit.append(j)
        lastvisit = newvisit
    res = []
    for i in outOrder:
        res.append(names[outOrder[i]])
    print(*res)

if __name__ == "__main__":
    testNO = int(input())
    for i in range(testNO):
        n,start = input().split(" ")
        n = int(n)
        name = input().split(" ")
        graph = []
        for j in range(n):
            lst = input().split(" ")
            lst = lst[1::]
            for k in range(len(lst)):
                lst[k] = int(lst[k])
            graph.append(lst)
        bfs(graph,start,name)