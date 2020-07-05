n, m = list(map(int, input().split()))
an = list(map(int, input().split()))
dictroad = {i + 1: [] for i in range(n)}
last = 0
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    dictroad[x].append(y)
    dictroad[y].append(x)


def search(cur, target, visited):
    if cur == target:
        return [[cur]]
    if cur in visited:
        return []
    retv = []
    visited.append(cur)
    for i in dictroad[cur]:
        newvisited = visited.copy()
        way = search(i, target, newvisited)
        if len(way) > 0:
            for x in way:
                A = [cur]
                A.extend(x)
                retv.append(A)
    return retv


for i in range(m):
    u, v, k = list(map(int, input().split()))
    print(u, v, k)
    print(n)
    u = u ^ last
    indexes = search(u, v, [])[0]
    last = sorted(an[a - 1] for a in indexes)[k - 1]
    print(last)

