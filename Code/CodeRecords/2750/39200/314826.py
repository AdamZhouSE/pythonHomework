n = int(input())
pairs = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("], [")]
d = {i : [] for i in range(n)}
for x in pairs:
    d[x[0]].append(x[1])
    d[x[1]].append(x[0])


def search(cur, visited):
    if cur in visited:
        return 1
    visited.append(cur)
    retv = [0]
    for x in d[cur]:
        if x not in visited:
            retv.append(search(x, visited))
    return 1 + max(retv)

minh = n + 1
res = []
for x in range(n):
    h = search(x, [])
    if h < minh:
        minh = h
        res = [x]
    elif h == minh:
        res.append(x)
print(res)
