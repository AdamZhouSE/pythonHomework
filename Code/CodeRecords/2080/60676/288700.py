def level_order(root: int):
    # 队列
    q = [root]
    res = []
    while len(q) != 0:
        for node in q:
            res.append(nodes[node])
        length = len(q)
        for l in range(length):
            # 将同层节点依次出队
            node = q.pop(0)
            for next_node in graph[node]:
                if nodes[next_node] not in res and next_node not in q:
                    q.append(next_node)
    return res


if __name__ == '__main__':
    ans = []
    for i in range(eval(input())):
        tmp = input().split()
        n = int(tmp[0])
        src = tmp[1]
        nodes = input().split()
        graph = [[] for j in range(n)]
        for j in range(n):
            line = input().split()
            for k in range(1, len(line)):
                graph[j].append(int(line[k]))
                graph[int(line[k])].append(j)
        ans.append(level_order(nodes.index(src)))
    for i in ans:
        for j in range(len(i) - 1):
            print(i[j], end=' ')
        print(i[-1])