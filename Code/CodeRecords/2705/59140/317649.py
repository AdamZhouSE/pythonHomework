def find(f, x):
    f.setdefault(x, x)
    if f[x] != x:
        f[x] = find(f, f[x])
    return f[x]


def cycle(graph):
    f = {}
    for x, y in graph:
        if find(f, x) == find(f, y):
            return True
        else:
            f[find(f, y)] = find(f, x)

temp=input()[2:-2].split("], [")
ans=[]
for i in temp:
    ans.append([int(x) for x in i.split(",")])
indegree = {i: 0 for i in range(1, len(ans) + 1)}
tmp = 0
for i, j in ans:
    indegree[j] += 1
    if indegree[j] == 2:
        tmp = j
        break
if tmp == 0:
    f = {}
    for x, y in ans:
        if find(f, x) == find(f, y):
            print([x,y])
            break
        else:
            f[find(f, y)] = find(f, x)
else:
    for x, y in ans[::-1]:
        if y == tmp:
            if not cycle(ans[:ans.index([x, y])] + ans[ans.index([x, y]) + 1:]):
                print([x, y])
                break
