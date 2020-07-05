n = int(input())
ai = list(map(int, input().split()))
dictroad = {i : [] for i in range(n)}
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    dictroad[x - 1].append(y - 1)
    dictroad[y - 1].append(x - 1)

def search(cur, target, visited):
    if cur == target:
        return [[]]
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
candy = [0 for i in range(n)]
for i in range(len(ai) - 1):
    ways = search(ai[i] - 1, ai[i + 1] - 1, [])
    ways = sorted(ways, key = lambda x:len(x))
    for r in ways[0]:
        candy[r] += 1
for i in candy:
    print(i)
