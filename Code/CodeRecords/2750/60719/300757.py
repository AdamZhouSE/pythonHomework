def get(n, edges):
    import collections
    if n == 1:
        return [0]
    leaves = collections.defaultdict(set)
    for u, v in edges:
        leaves[u].add(v)
        leaves[v].add(u)
    q = collections.deque()
    for u, v in leaves.items():
        if len(v) == 1:
            q.append(u)
    while n > 2:
        l = len(q)
        n -= l
        for i in range(l):
            u = q.popleft()
            for v in leaves[u]:
                leaves[v].remove(u)
                if len(leaves[v]) == 1:
                    q.append(v)
    return list(q)


nums = int(input())
edges = eval(input())
res = get(nums, edges)
print(res)