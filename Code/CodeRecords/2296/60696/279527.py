lch = []
rch = []
paths = []
value = []
goal = 0


def get_path(root, s, total):
    if root == 0:
        return
    s.append(root)
    total += value[root]
    if total == goal:
        paths.append(s.copy())
    if lch[root] != 0:
        get_path(lch[root], s, total)
        get_path(lch[root], [], 0)
    if rch[root] != 0:
        get_path(rch[root], s, total)
        get_path(rch[root], [], 0)
    s.pop(-1)


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    root = arr[1]
    lch = [0 for i in range(101)]
    rch = [0 for i in range(101)]
    value = [0 for i in range(101)]
    for i in range(n):
        arr = [int(j) for j in input().split()]
        lch[arr[0]] = arr[1]
        rch[arr[0]] = arr[2]
        value[arr[0]] = arr[3]
    goal = int(input())
    get_path(root, [], 0)
    res = 0
    for path in paths:
        res = max(res, len(path))
    print(res)