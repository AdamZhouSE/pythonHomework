
def fson(paths: dict, son: dict, dad: int, res: list, n: int):
    if len(res) < n:
        for key in paths.keys():
            if paths[key].count(dad) > 0 and key not in res:
                son[dad].append(key)
                res.append(key)
                fson(paths, son, key, res, n)


def fdad(son: dict, dad: dict):
    for key in son.keys():
        for i in son[key]:
            dad[i].append(key)


def path(paths: dict, road: list, dst: int, res: list):
    if dst == res[-1]:
        road.append(res[:])
    else:
        for t in paths[res[-1]]:
            if t not in res:
                res.append(t)
                path(paths, road, dst, res)
                del res[-1]


def root(son: dict, roo: int, road: list):
    for t in son[roo]:
        road.append(t)
        root(son, t, road)


def func28():
    arr = list(map(int, input().split()))
    n, m, r, p = arr[0], arr[1], arr[2], arr[3]
    arr = list(map(int, input().split()))
    paths, ops = {i: [] for i in range(1, n + 1)}, []
    dad, son = {i: [] for i in range(1, n + 1)}, {i: [] for i in range(1, n + 1)}
    for i in range(0, n - 1):
        t = list(map(int, input().split()))
        paths[t[0]].append(t[1])
        paths[t[1]].append(t[0])
    fson(paths, son, r, [r], n)
    fdad(son, dad)
    for i in range(0, m):
        ops.append(list(map(int, input().split())))


    for t in ops:
        if t[0] == 1:
            res = []
            path(paths, res, t[2],[t[1]])
            for i in res[0]:
                arr[i - 1] += t[3]
        if t[0] == 2:
            res, ans = [], 0
            path(paths, res, t[2],[t[1]])
            for i in res[0]:
                ans += arr[i - 1]
            print(ans % p)
        if t[0] == 3:
            res = [t[1]]
            root(son, t[1], res)
            for i in res:
                arr[i - 1] += t[2]
        if t[0] == 4:
            res, ans = [t[1]], 0
            root(son, t[1], res)
            for i in res:
                ans += arr[i - 1]
            print(ans % p)


func28()
