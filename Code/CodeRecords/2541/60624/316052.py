def func20():
    n = int(input())
    in_str = input().strip()[1:-1]
    p = []
    while True:
        start = in_str.find("[")
        if start == -1:
            break
        end_ = in_str.find("]")
        p.append(list(map(int, in_str[start+1:end_].split(","))))
        in_str = in_str[end_+1:]
    length = len(p)
    if length == 0:
        print([i for i in range(n)])
        return
    in_degree = [0 for x in range(n)]
    adj = [set() for x in range(n)]
    for second,first in p:
        in_degree[second] += 1
        adj[first].add(second)
    res = []
    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    while queue:
        top = queue.pop(0)
        res.append(top)
        for successor in adj[top]:
            in_degree[successor] -= 1
            if in_degree[successor] == 0:
                queue.append(successor)
    if len(res) != n:
        print([])
    else:
        print(res)
    return 
func20()