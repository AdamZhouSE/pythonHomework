def search(num: int, ls: list) -> list:
    res = []
    indegrees = [0 for _ in range(num)]
    ajacency = [[] for _ in range(num)]
    for cur, pre in ls:
        indegrees[cur] += 1
        ajacency[pre].append(cur)
    deque = []
    for i in range(num):
        if indegrees[i] == 0:
            deque.append(i)
    while deque:
        cur = deque.pop(0)
        res.append(cur)
        for pre in ajacency[cur]:
            indegrees[pre] -= 1
            if indegrees[pre] == 0:
                deque.append(pre)
    return res


n = int(input())
lst = eval(input())
print(search(n, lst))