def travel(f, record, add_sum):
    if f == (ns - 1, ns - 1):
        paths.append(min(add_sum + lst[f[0]][f[1]], record))
        return
    else:
        ds = [[0, 1], [1, 0]]
        for d in ds:
            if 0 <= f[0] + d[0] < ns and 0 <= f[1] + d[1] < ns:
                nx, ny = f[0] + d[0], f[1] + d[1]
                travel((nx, ny), min(add_sum + lst[f[0]][f[1]], record), add_sum + lst[f[0]][f[1]])


ns = int(input())
lst = []
for n in range(ns):
    lst.append(list(map(int, input().split(','))))
paths = []
travel((0, 0), 0, 0)
print(max(1, 1 - max(paths)))
