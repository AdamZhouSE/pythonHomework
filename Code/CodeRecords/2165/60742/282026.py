t = int(input())
for k in range(t):
    n,begin = input().split()
    n = int(n)
    nodes = input().split()
    a = []
    for i in range(n):
        a.append([int(i) for i in input().split()[1:]])
    res = []
    queue = [begin]
    while queue:
        top = queue.pop(0)
        res.append(top)
        idx = nodes.index(top)
        for i in range(n):
            if a[idx][i]==1 and nodes[i] not in queue and nodes[i] not in res:
                queue.append(nodes[i])
    print(' '.join(res))