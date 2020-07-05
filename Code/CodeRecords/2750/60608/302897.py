
def high(res: dict, path: list, level: int, val: list):
    val[0] = max(val[0], level)
    for dot in res[path[-1]]:
        if dot not in path:
            path.append(dot)
            high(res, path, level + 1, val)
            del path[-1]


def func7():
    n, arr = eval(input()), eval(input())
    res, ans, val, level = {i: [] for i in range(0, n)}, [], [0], n
    for node in arr:
        res[node[0]].append(node[1])
        res[node[1]].append(node[0])
    for i in range(0, n):
        val = [1]
        path = [i]
        high(res, path, 1, val)
        if level == val[0]:
            level = val[0]
            ans.append(path[0])
        elif level > val[0]:
            level = val[0]
            ans = [path[0]]

    print(ans)


func7()
