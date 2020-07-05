def destruct_tree():
    if k == 1:
        return 'YES'
    if n % k != 0:
        return 'NO'
    else:
        edges = n - 1
        while edges > 0:
            for i in range(N):
                if len(graph[i]) == 1:
                    if weights[graph[i][0]] == k:
                        return 'NO'
                    weights[graph[i][0]] += weights[i]
                    weights[i] = 0
                    graph[graph[i][0]].remove(i)
                    graph[i].clear()
                    edges -= 1
            for i in range(N):
                if weights[i] == k:
                    weights[i] = 0
        for i in range(N):
            if 0 < weights[i] < k:
                return 'NO'
        return 'YES'


if __name__ == '__main__':
    res = []
    for t in range(int(input())):
        nk = input().split()
        n = int(nk[0])
        # 扩大数据表示范围
        N = 2 * n
        k = int(nk[1])
        graph = [[] for i in range(N)]
        weights = [0 for i in range(N)]
        for i in range(n-1):
            edge = input().split()
            graph[int(edge[0]) - 1].append(int(edge[1]) - 1)
            graph[int(edge[1]) - 1].append(int(edge[0]) - 1)
            weights[int(edge[0]) - 1] = 1
            weights[int(edge[1]) - 1] = 1
        res.append(destruct_tree())
    for t in res:
        print(t)