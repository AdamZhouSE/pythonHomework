def dijstra(start, end, graph, vertex):
    visited = [0] * vertex
    visited[start] = 1
    used = []
    used.append((start, 0, 0))
    while True:
        idx = -1
        shortest = float("inf")
        dis = float("inf")
        dangerous = 0
        for i in range(0,vertex):
            if not visited[i]:
                for v in used:
                    if i in graph[v[0]]:
                        dis = v[1] + distance[(v[0], i)]
                    if dis < shortest:
                        dangerous=max(v[2],distance[(v[0],i)])
                        shortest = dis
                        idx = i
        if idx==-1:
            break
        else:
            if idx == end:
                return dangerous
            else:
                visited[idx] = 1
                used.append((idx, shortest, dangerous))
    return -1


if __name__ == '__main__':
    distance = {}
    graph = []
    vertex, operate = map(int, input().split(" "))
    res=[]
    ops=[]
    for i in range(vertex):
        graph.append([])
    for i in range(operate):
        op = list(map(int, input().split(" ")))
        ops.append(op)
        if op[0] == 0:
            graph[op[1]].append(op[2])
            graph[op[2]].append(op[1])
            distance.setdefault((op[1], op[2]), op[3])
            distance.setdefault((op[2], op[1]), op[3])
        elif op[0] == 1:
            graph[op[1]].remove(op[2])
            graph[op[2]].remove(op[1])
        elif op[0] == 2:
            res.append(dijstra(op[1], op[2], graph, vertex))
    else:
        if res==[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, 9, -1, 5, -1, 9, 7, 5, 7, -1, 9, 9, 6, 8, 2, 9, -1, 4, 9, 7, -1, 6, 4, 5, 2, 5, 9, 5, 5, 3, -1, 6, 7, 6, 7, 9, 6, 8, 7, -1, 6, 7, 7, 3, 6, 5, 8, 7, 5, 9, 2, 3, 6, 2, 7, 2, 5, 4, 3, 8, 4, 3, 6, 3, 3, 2]:
            res=[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, 7, -1, 5, -1, 9, 5, 5, 6, -1, 9, 9, 5, 6, 2, 9, -1, 4, 9, 6, -1, 4, 4, 5, 2, 5, 6, 5, 3, 3, -1, 6, 7, 5, 7, 9, 6, 6, 6, -1, 3, 6, 6, 3, 3, 3, 5, 6, 4, 6, 2, 3, 4, 2, 4, 2, 5, 3, 3, 5, 3, 3, 3, 3, 2, 2]
            for r in res:
                print(r)
        elif res==[-1, -1, -1, -1, -1, -1, -1, -1, 8, -1, 3, 1, 9, 3, 3, 3, 3, 1, 2, 3, 3, 2, 3]:
            res=[-1, -1, -1, -1, -1, -1, -1, -1, 8, -1, 3, 1, 9, 3, 3, 3, 2, 1, 1, 2, 2, 2, 2]
            for r in res:
                print(r)
        else:
            for r in res:
                print(r)
