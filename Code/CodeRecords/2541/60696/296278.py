"""
拓扑排序
"""

if __name__ == '__main__':
    n = int(input())
    edges = [[] for i in range(n)]
    in_degree = [0] * n
    conditions = eval(input())
    for i in range(len(conditions)):
        edges[conditions[i][1]].append(conditions[i][0])
        in_degree[conditions[i][0]] += 1
    Q = []
    res = []
    for i in range(n):
        if in_degree[i] == 0:
            Q.append(i)
    cnt = 0
    while len(Q) != 0:
        cnt += 1
        top = Q.pop(-1)
        res.append(top)
        for i in range(len(edges[top])):
            in_degree[edges[top][i]] -= 1
            if in_degree[edges[top][i]] == 0:
                Q.insert(0, edges[top][i])
    if cnt == n:
        print(res)
    else:
        print([])