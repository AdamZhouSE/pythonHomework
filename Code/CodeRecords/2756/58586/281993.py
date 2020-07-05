def bfs(graph, root):
    visited=[]
    type = 0
    color = 0
    queue = []
    distance = 0
    res[root][type] = 0
    queue.insert(0, root)
    while len(queue) > 0:
        size = len(queue)
        distance += 1
        for i in range(size):
            node = queue.pop()
            visited.append(node)
            for e in graph[color][node]:
                if e not in visited:
                    res[e][type] = distance
                    queue.insert(0, e)
                    visited.append(e)
        color = (color + 1) % 2
    visited.clear()
    color, type = 1, 1
    while len(queue) > 0:
        size = len(queue)
        distance += 1
        for i in range(size):
            node = queue.pop()
            visited.append(node)
            for e in graph[color][node]:
                if e not in visited:
                    res[e][type] = distance
                    queue.insert(0, e)
                    visited.append(e)
        color = (color + 1) % 2


if __name__ == '__main__':
    n = int(input())
    red = eval(input())
    blue = eval(input())
    red_graph, blue_graph = [], []
    for i in range(n):
        red_graph.append([])
        blue_graph.append([])
    for e in red:
        red_graph[e[0]].append(e[1])
    for e in blue:
        blue_graph[e[0]].append(e[1])
    graph = [red_graph, blue_graph]
    res = [[10001, 10001] for i in range(n)]
    bfs(graph,0)
    ans=[]
    for i in range(len(res)):
        temp = min(res[i][0], res[i][1])
        a = temp if temp != 10001 else -1
        ans.append(a)
    print(ans)
